# `arcane` access modifier

```php
  #[VisibleFor(Class1::class, Class2::class)]
  arcane function someMethod(): void
  {

  }
```

This is particularly useful for DDD when we want to build strict domain model, which doesn't allow external modification. I mean this model doesn't have to expose methods which it use inside to interact into pulic world. But currently Domain Models can't interact one with another unless they make their methods public. Public methods tempt to use them (they are intended to be used from outside. But when it comes to some Unit, build from couple of classes, personally I would like to hide all this methods used only for internal interaction from my IDE completion list. This makes code less error prone.


I suggest name `arcane`, because it's meaning is "understood by few; mysterious or secret". This "understood by few" really fits because we expose method for two or so classes. And client code doesn't have to understand `arcane` methods.

