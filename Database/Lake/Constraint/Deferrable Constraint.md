---
aliases:
  - Deferred Constraint
---
In [[PostgreSQL]] it's possible to create Deferrable constraints.
Particularly it's useful to overcome [[Doctrine ORM]]'s limitations:
- [[Entity deletion happens last]];
- [[Doctrine ORM Change Entity Discriminator Column]].

Specialities:
- [[Deferrable Primary Key Constraint]]
- [[Deferrable Partial Unique Constraint]]
