In most cases it is composed of primitive values or other value objects, but Value Object can even reference entities. For instance a RespondentFilter that could hold references to City, WorkPosition, Department is still a value-object.

When using Doctrine ORM the only way to map such objects to the database is by marking them as entities.

