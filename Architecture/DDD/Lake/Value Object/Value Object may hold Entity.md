In most cases it is composed of primitive values or other value objects, but Value Object can even reference entities. 

> VALUE OBJECTS can even reference ENTITIES.
> (chapter 5)

For instance a `RespondentFilter` could hold references to `City`, `Position`, `Unit`, and still be a value-object.

When using Doctrine ORM the only way to map such objects to the database is by marking them as entities ([[Long face.png]]).

In this example, Delivery Specification is a [[Value Object]] that references Location entity.
![[Value Object holding Entity.png]]