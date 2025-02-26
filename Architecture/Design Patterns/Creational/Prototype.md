Prototype allows you to create new object from existing objects without tightly coupling client code up to the internal [[Encapsulation|encapsulated]] structure of the objects.

Basically this is the implementation of `clone()` method that creates new instance with cloned nested structure as well.

Example use case is when customer asks us to create a new Notification Campaign based on the existing one.
