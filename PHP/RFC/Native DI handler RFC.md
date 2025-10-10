
# Native Dependencies Handler (`__inject`)

## Introduction
Currently there are a lot of third-party libraries for handling class dependencies. But the problem with them is they are not going to work if you instantiate object with `new` keyword. To actually use dependencies container, we need create objects with helper function. Thereby, when requirements are changed and class need additional dependency, we will need to wade through all places where objects of that class are created in native way (we couldn't enforce using helper function to make our objects).

### In general, we can spot two main types of dependencies:
1. Class-based - independent of surroundings, but depends rather on _class name_ - for each  object being instantiated we want to use the same strategy of creating those dependencies;
2. Runtime-based - can only be provided accordingly to some _external conditions_ known only right before object is created.

## Proposal
### In a nutshell:
Besides the constructor, we introduce new magic method `__inject` to inject [runtime-independent (class-based)](#in-general-we-can-spot-two-main-types-of-dependencies) dependencies in according to the registered configuration.

Every time `new` keyword is used, right before `__construct` is invoked, dependencies will be resolved and given to `__inject` method. Constructor like before accepts arguments given in brackets near `new` keyword.

### More verbose explanation:
It was considered to register dependencies directly for constructor and mix runtime- and class-dependent parameters in `__construct`, but it seems that code will become very tangled and confusing because you don't certainly know where which parameter came from. And also IDE would not be able to spot which parameter where goes.

The better approach is just left `__construct` as it always was used (for runtime-dependent values). And for all dependencies which have nothing to do with runtime context, use separate magic method  `__inject`. 

#### Let's look at simple example when dependencies grow:
1. At the start we have password, represented by it's raw value:
```php
class UserPassword
{
    public function __construct(
        private string $value
    ){}
    // ...
}
// a lot of places where it is created
$password = new UserPassword('qwerty');
```
2. Then, for security reasons we decided to hash passwords, thus new `HasherInterface` dependency is required. We know that for every object of `UserPassword` we want use the same type of hasher - or even same object (dependency is class-based). So we add dependency into `__inject` method:
```php
class UserPassword
{
    public function __inject(
        private HasherInterface $hasher
    ){ }
    
    public function __construct(
        private string $value,
        bool $alreadyHashed = false
    ){
        if (!$alreadyHashed) {
            $this->value = $this->hasher->make($value);
        }
    }

    // ...
}
```
> Note about the moment when `__inject` is called. As it is used for runtime-independent values, it has to be called right before `__construct` so that in constructor we can use all given dependencies.
3. Once we declared `__inject` method, we need to configure container. To register dependencies configuration, we implement `DependenciesProvider` and place all registrations into `registerBindingsTo` method:
```php
class ApplicationDependenciesProvider implements DependenciesProvider  
{
  public function registerBindingsTo(DependenciesRecorder $recorder): void  
  {
        $recorder->when(UserPassword::class)
            ->needs(HasherInterface::class)
            ->provide(Sha256Hasher::class);
        
        $recorder->singleton(Sha256Hasher::class);
    }
}
```
> For more configuration examples, see [Dependency bindings](#possible-dependency-bindings)

And then, we pass instance of created provider into special function:
```php
register_dependency_bindings(new ApplicationDependenciesProvider());
```
4. As result, all previous code is not broken and we don't have to modify it.
```php
// [old code] in a lot of places (now hasher is automatically injected)
$password = new UserPassword('this string will be hashed');

// no troubles with providing class-based dependencies
$passwordFromDB = new UserPassword(
    'SGVsbG8sIGZyaWVuZC4gV2h5IGFyZSB5b3UgaGVyZT8gQHJlbGE1ODlu',
    alreadyHashed: true
);
```
If for some odd reason (or for unit testing) we need customize dependencies in `__inject` method at runtime, it could be done by means of named arguments. 
```php
$password = new UserPassword( 
    'some text here',
    hasher: new Argon2IdHasher()
);
```
> _Note:_ When you find yourself customizing dependencies in `__inject`, reconsider if they really can't reside in constructor.

At first, PHP tries to locate named parameter in _constructor_ but if not found, looks for it in _inject method_.  If match established, value will be passed into _injector_ and thus override registered binding for this parameter.

#### How does actual creating works
Let's consider previous code snippet.

As usual, PHP prepare all provided parameters (string `'some text here'` will be considered as `$value` and default value `false` will be used for `$alreadyHashed`). 

When php face named argument which is not bound to constructor parameter, it tries to locate corresponding argument match in signature of _inject_ method. If it was found, that extra argument will be used to satisfy dependency. Those extra values are stored somewhere (probably `HashMap`) until actually invoking _injector_.

So, all arguments for constructor are prepared and stored. And also we have extra dependencies which override configuration of providing defined in _DependenciesProvider_. 
At this point, `__inject` will be called in the following way. Go through all expected parameters and if for current expected argument exists extra value in `HashMap`, then give that value and remove it from map. Else resolve dependency in accordance with registered bindings if such are provided. 

If there is no configuration provided for class, PHP will try to create object as it is (and if needed, analyze and resolve it's own dependencies, dependencies of dependencies and so forth). If object or some of it's dependencies could not be instantiated, some kind of Exception will be generated.
> For more information see [injecting](#how-php-will-inject-dependencies).

### Possible dependency bindings:

1. Global binding Interface (or Abstract class) to implementation:
```php
$recorder->bind(
    ArticlesRepository::class,
    CachedArticlesRepositoryDecorator::class
);
```
Wherever `ArticlesRepository` is required, `CachedArticlesRepositoryDecorator` will be used (unless we defined more specific binding - see item 4). When it is time to pass dependencies, PHP will try to build `concretion` (cache decorator in example) by himself (analyzing it's dependencies and so on). To specify own strategy of creating, consider `defineCreatingStrategy` method (see below).

2. Defining global strategy how to create object of particular class (by default, php will try to create object by [analyzing](#how-php-will-inject-dependencies) all dependencies and providing them):
```php
$recorder->defineCreatingStrategy(
    Argon2IdHasher::class,
    fn () => new Argon2IdHasher([
        'verify' => true
    ])// Argon2Hasher dependencies described in __inject will be also provided
);
```
3. Defining a singleton. Object will be created once, next times the same will be used. It doesn't apply for those bindings where `resolve` is used, because in function we have full control over  supplying object.
```php
$recorder->singleton(DatabaseConnection::class);
```
> To define own strategy for creating singleton object, use `defineCreatingStrategy`.
4. Contextual binding. Use `when - needs - provide` notation to define which implementation should be used. PHP will try to build bound object by [analyzing](#how-php-will-inject-dependencies) it's `__inject` method.
```php
$recorder->when(UserPassword::class)
    ->needs(HasherInterface::class)
    ->provide(Sha256Hasher::class);
```
>Note that strategy of creating `Sha256Hasher` can be defined with `defineResolveStrategy` method described above. Or else, you can use `resolve` instead of `provide`. 

Instead of `provide`, you can use`give` method, where you pass instantiated object
```php
$recorder->when(StoreFileRequest::class)
    ->needs(FileDescriptionRules::class)
    ->give($loadedFromCacheFileDescriptionRules)
```
> This is useful if you would like eager load your objects or use caching for some configuration objects which take a lot of time to build.
5. Contextual binding with custom `resolve` strategy (singletons don't apply for such binding, cuz we have full control over method):
```php
$recorder->when(PlayWithEvents::class, EventMocker::class)
    ->needs(EventsDispatcher::class)
    ->resolve(fn() => new EventFake(eventsToFake: '*'));
```
Take a look at `when` method, which accepts variadic array of classes dependent of `EventsDispatcher`. Thus, when `PlayWithEvents` and other classes will be created, they will be provided with `EventFake` implementation of `EventsDispatcher` interface unless binding is overridden by further one (for example, simple `when - needs - resolve` for some particular class).

6. Contextual parameters bindings. We can bind concrete values (or strategies of acquiring them) to variable names of  `__inject` method.
```php
$recorder->when(RegisterUserCommand::class)
    ->asksGive(sendEmail:    true, 
               startSession: true)
    ->asksGive(notifyAdmin: AdminNotifier::IF_NOT_NIGHT)
    ->asksResolve(emailDriver: fn() => new SwiftEmailDriver());
```
As you can see, `asksGive` method accepts variadic array with named parameters, values of which will be given to `RegisterUserCommand`.
Also, we can use `asksResolve`, where each value must be callback returning desirable parameter value. It is useful when we want to create objects (callback will be invoked at runtime, therefore all bindings are registered).

7. Binding typed variadics. Consider next example:
```php
class Firewall
{
    private array $filters;
    
    public function __construct(
	private Logger $logger, 
                Filter ...$filters)
    { 
    	$this->filters = $filters;
    }
}
```
To register variadic binding, we have pleasant `needsVariadic` method:
```php
$this->when(Firewall::class)
    ->needsVariadic(Filter::class)
    ->resolve(fn() => [
        new BannedUsersFilter(),
        new BannedByIpFilter(BannedByIpFilter::WEAK_STRATEGY)
    ]);
```
We can use either `resolve` or `give` method. Difference is that `resolve` always accepts callback, thus all objects will be created just before injecting. From other hand, `give` method _gives_ actual values, therefore all objects will be created right away during configuration long before they actually needed. For objects, it is better to use `resolve` method inasmuch as all bindings will be registered when it's time to create.

Variadic primitives example:
```php
$this->when(Refrigerator::class)
    ->needsVariadic('int')
    ->give([
        89,
        97,
    ]);
```
> Note: another (and maybe better for primitives) option to inject variadic parameter is to use binding by parameter names (see item 6)
8. Extending bindings. The `extend` method allows the mutation of resolved services. For example, when a service is resolved, you may run additional code to decorate or configure the service. Method accepts `Closure`, which which will be given with created object and must return one of it's instance. The returned value will be actually used.
```php
$this->extend(
    ExternalService::class,
    function (ExternalService $service): ExternalService {
        $service->setSomeDependency(new SomeDependency());

        return new DecoratedService($service);
    }
});
```
> Note that every time `ExternalService` is instantiated, will be used our own implementation. It gives us a bit control over third-party libraries which will use `__inject` method so that we can substitute objects with our own implementation or configuration. We should be careful and don't overuse this.

### Resolving dependencies
When need to provide dependency in obedience to binding, need to follow next order of checking:
1. Contextual binding by parameter name (`asksGive`, `asksResolve`);
2. Contextual variadic binding (`give`, `resolve`);
3. Contextual binding by class name (`give`, `provide`, `resolve`);
4. Global binding abstraction to implementation (`bind`, `defineCreatingStrategy`).

#### How php will inject dependencies
For example, if we had code snippet:
```php
class UserPassword
{
    public function __provide(
        private HasherInterface $hasher
    ){ }

    public function __construct(
        private string $value,
        bool $alreadyHashed = false
    ) {
        if (!$alreadyHashed) {
            $this->value = $this->hasher->make($value);
        }
    }

    // ...
}
```
In the main code, we instantiate `UserPassword` like this:
```php
$password = new UserPassword('hello, world!');
```
If run code like this, Exception will be generated, because we didn't register binding for hasher. It could be done in multiple ways, like shown [above](#possible-dependency-bindings).
Let's use contextual binding by class name:
```php
$recorder->when(UserPassword::class)  
    ->needs(HasherInterface::class)  
    ->provide(Sha256Hasher::class);
```
When php creates object, there are two possible options for hasher dependency:
1. If we defined strategy of resolving `Sha256Hasher`, then it will be used.
2. If not, everything is a little more complicated.
PHP sees that there is no strategy for resolving `Sha256Hasher`, thus will optimistically try to instantiate it and satisfy it's dependencies. 
2.1 If class is abstract or an interface, will be thrown error;
2.2 If constructor has required parameter, then we could not satisfy it and  error will be thrown;
2.3 Else php will traverse all expected parameters of `__inject` and try to find bindings for this parameter. If it found, PHP create dependency accordingly to it. Else repeats the same algorithm described here.

Consider signatures of `__inject` and `__construct` of `Sha256Hasher`:
```php
class Sha256Hasher
{
    public function __inject(
        private NumbersShifter $numbersShifter
    ) {}

    public function __construct(int $times = 1)
    {
        //
    }
}
```
We can try to build it, because constructor has all parameters as optional.
`NumbersShifter` - real class, which could be instantiated and built, so it  will be done and PHP will inject it into our hasher.

## Backward Incompatible Changes
Code will get broken if:
1. Class had `__inject` method;
2. Function `register_dependency_bindings` was declared;
3. Any of the classes used by Container were declared.

## Impact On Performance
- For already working code in fact there is no impact. Every time `__construct` called,  empty `__inject` method will be called right before. Thus, it is insignificant.
- For new code, which would use dependencies handler at full power, creating objects will slow down a little bit  (time to find out bindings and resolving strategies). In either way, speed depends on implementation.
## Proposed PHP Version(s)
PHP 8
## Implementation blueprint
Signature of `register_dependency_bindings` function:
```php
function register_dependency_bindings(DependenciesProvider $provider)  
{  
  // ..  
}
```
Note that we should be able to register dependencies from multiple providers. For example, third party libraries might also want to use dependencies container for their work. Thus, all dependency recorders should work with the same storage of dependencies.

`DependenciesProvider` must be an interface class like so:
```php
interface DependenciesProvider  
{  
    public function registerBindingsTo(DependenciesRecorder $recorder): void;  
}
```
Dependencies Recorder:
```php
class DependenciesRecorder implements RegistersContainerDependencies
{
    private DependenciesContainer $container;

    // delegate all registrations to container
}
```
Interfaces for registering bindings:
```php
interface RegistersContainerDependencies extends RegistersContextualBindings, 
                                                 RegistersGlobalDependencyBindings,
                                                 RegistersDependencyExtensions, 
                                                 RegisterDependenciesAsLimited
{

}

interface RegistersContextualBindings  
{  
    public function when(string ...$concretes): ContextualBindingBuilder;  
}

interface RegistersGlobalDependencyBindings  
{  
    public function bind(string $abstract, string $concrete): void;  
  
    public function defineCreatingStrategy(string $className, \Closure $how): void;  
}

interface RegistersDependencyExtensions  
{  
    public function extend(string $concrete, \Closure $how): void;  
}

interface RegisterDependenciesAsLimited  
{  
    public function singleton(string... $concrete): void;  
}
```
Main Dependencies Container:
```php
class DependenciesContainer implements RegistersContainerDependencies  
{  
  private ContextualDependencyBindingsContainer $contextualBindingsContainer;  
  private GlobalDependencyBindingsContainer $globalBindingsContainer;  
  private DependencyExtensionsContainer $dependencyExtensionsContainer;  
  private LimitedDependenciesInspector $limitedDependenciesContainer;  
  
  // work with smaller containers, resolve dependencies for classes, ...
}
```
Smaller containers:
```php
final class ContextualDependencyBindingsContainer implements RegistersContextualBindings,
                                                             \Psr\Container\ContainerInterface
{
    //
}

final class GlobalDependencyBindingsContainer implements RegistersGlobalDependencyBindings,
                                                         \Psr\Container\ContainerInterface
{

}


final class DependencyExtensionsContainer implements RegistersDependencyExtensions, 
                                                     \Psr\Container\ContainerInterface
{
    //
}

final class LimitedDependenciesInspector implements RegisterDependenciesAsLimited
{
    public function isSingleton(string $concrete)
    {
    
    }
    //
}
```
Contextual Binding Builder:
```php
interface ContextualBindingBuilder  
{  
  public function needs(string $abstract): ContextualClassBindingBuilder;  
  
  public function needsVariadic(string $typeName): ContextualVariadicTypeBindingBuilder;  
  
  public function asksGive(...$keysValues): static;  
  
  public function asksResolve(\Closure ...$resolvers): static;  
}
```
Contextual Class Binding Builder:
```php
interface ContextualClassBindingBuilder  
{  
    public function provide(string $concrete): void;  

    public function give($value): void;

    public function resolve(\Closure $strategy): void;  
}
```
Contextual Variadic Type Binding Builder:
```php
interface ContextualVariadicTypeBindingBuilder
{
    public function give(array $values): void;

    public function resolve(\Closure $strategy): void;
}
```
## Requirements
To implement such functionality, the next features are required:
- Named arguments ([RFC](https://wiki.php.net/rfc/named_params));


