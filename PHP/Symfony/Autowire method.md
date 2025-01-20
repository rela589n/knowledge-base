---
aliases:
  - Symfony autowire method
---

Symfony allows autowiring for controller methods.

It does so by means of `\Symfony\Component\HttpKernel\Controller\ArgumentResolver\ServiceValueResolver` that uses arguments locator one per each controller:

```php
return [$this->container->get($controller)->get($argument->getName())];
```

The controller locators are built in `\Symfony\Component\HttpKernel\DependencyInjection\RegisterControllerArgumentLocatorsPass`:

```php
if ($autowireAttributes) {  
    $attribute = $autowireAttributes[0]->newInstance();  
    $value = $parameterBag->resolveValue($attribute->value);  
  
    if ($attribute instanceof AutowireCallable) {  
        $args[$p->name] = $attribute->buildDefinition($value, $type, $p);  
    } elseif ($value instanceof Reference) {  
        $args[$p->name] = $type ? new TypedReference($value, $type, $invalidBehavior, $p->name) : new Reference($value, $invalidBehavior);  
    } else {  
        $args[$p->name] = new Reference('.value.'.$container->hash($value));  
        $container->register((string) $args[$p->name], 'mixed')  
            ->setFactory('current')  
            ->addArgument([$value]);  
    }  
    continue;  
}
```

Here, `parameterBag` is used to resolve placeholders.

Basically, the main condition here is `$value instanceof Reference`, since it gives us `Reference` to the needed service.

Later on `$args` are used to register service locator for this particular controller:

```php
$controllers[$id.'::'.$r->name] = ServiceLocatorTagPass::register($container, $args, ...);
```

Hence, we could say that every time container is built, these arguments are resolved for every controller that needs to autowire anything in the method.