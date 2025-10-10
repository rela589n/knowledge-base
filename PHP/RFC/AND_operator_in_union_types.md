
When you follow ISP, you propably would have a lot of interfaces. 
Thus, client code may require an object to implement a bunch of interfaces depending on functionality needed.

Consider class `Bar`:

```php

interface A {}

interface B {}

interface C {}

interface D {}

interface E {}

class Bar implements A, B, C, D, E {
    // 
}
```


And some code, which uses `Bar`, but depends rather on interfaces, which functionality is actually needed:

```php
function foo(A & B & E $object) {
  // some work
  
  var_dump($object);
}
```

It is currently feasable like this (ugly):

```php
function foo(A $object) {
  (function(B $object) {
    
    (function(E $object) {
      
        // some work
        
        var_dump($object);
      
    })($object);
    
  })($object);
}
```

Or like this (more readable, but still):

```php
function foo(A | B | E $object) {
  
  if (!$object instanceof A) {
    throw new \RuntimeException();
  }  
  
  if (!$object instanceof B) {
    throw new \RuntimeException();
  }
  
  if (!$object instanceof E) {
    throw new \RuntimeException();
  }  
 
  // some work
  
  var_dump($object); 
}
```

This idea proposes to eliminate `instanceof` checks by introducing `&` union operator.

