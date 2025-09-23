Entity manager [leaks memory](https://youtu.be/2HAGlULliyI?si=MKv4nZxX9TrUIiCH&t=1140):

![[Entity manager leaks.png]]

Method in `EntityManager.php`:
```php
public function getRepository(string $className): EntityRepository
{
    return $this->repositoryFactory->getRepository($this, $className);
}
```

If you are to decorate Entity Manager, good luck in sorting out memory leaks and side effects. Even if you have decorated it, the repositories will still have the inner "real" entity manager that was never decorated.

This is the problem of implicit `$this`. If it was explicit, one could've just passed it from `EntityManagerDecorator::getRepository()` method into the inner entity manager.
 
```php
public function getRepository(string $className): EntityRepository  
{  
    return $this->wrapped->getRepository($className);  
}
```

Another solution could be writing `Closure` over wrapped entity manager that is bound to `$this` of entity manager decorator. Hence, it could've worked if PHP allowed this 🙁.