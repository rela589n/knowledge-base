---
aliases:
  - Deferred Constraint
---
**Deferrable Constraint** allows to **defer the validation** 
of the [[Consistency]] rule *until* the **end of [[Transaction]]**.

Supported by [[PostgreSQL]].

Particularly useful to overcome [[Doctrine ORM]]'s limitations:
- [[Entity deletion happens last]];
- [[Doctrine ORM Entity Change Discriminator Column]].

Specialities:
- [[Deferrable Primary Key Constraint]]
- [[Deferrable Partial Unique Constraint]]
