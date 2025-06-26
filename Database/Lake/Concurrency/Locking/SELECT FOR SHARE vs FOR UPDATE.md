---
aliases:
  - Shared Lock
---
[[Explicit locking|SELECT FOR UPDATE]] prevents other [[Transaction|Transactions]] from doing [[Explicit locking|SELECT FOR UPDATE]], `UPDATE`, `DELETE`.

`SELECT FOR SHARE` doesn't prevent another [[Transaction]] from `SELECT FOR SHARE`, but does prevent [[Explicit locking|SELECT FOR UPDATE]], `UPDATE`, `DELETE`.

![[Row-level locks.png]]