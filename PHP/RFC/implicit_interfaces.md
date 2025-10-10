Currently if code is dependant on interface, objects must explicitly declare `implements` in their class.
But if we would like to create interface for framework class, we need to create own implementation.

There already are `implicit` interfaces (like Stringable).

Also, it may be interesting to implement segregated interfaces:

```
interface ObjectPersister segregates ObjectManager
{
  // signature must be compatible with ObjectManager::persist()
  public function persist($entity);
}
```

As far as our code depend on ObjectPersister, we see autocompletion only for persist method. But we accept any implementation of ObjectManager.

This somewhat resembles duck typing.




