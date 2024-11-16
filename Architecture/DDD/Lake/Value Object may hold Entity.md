In most cases it is composed of primitive values or other value objects, but Value Object can even reference entities. 

For instance a `RespondentFilter` could hold references to `City`, `Position`, `Unit`, and still be a value-object.

When using Doctrine ORM the only way to map such objects to the database is by marking them as entities ([[Disappointed face.png]].