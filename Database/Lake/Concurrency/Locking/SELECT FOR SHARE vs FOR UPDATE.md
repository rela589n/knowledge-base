`SELECT FOR UPDATE` prevents other transactions from doing `SELECT FOR UPDATE`, `UPDATE`, `DELETE`.

`SELECT FOR SHARE` doesn't prevent another transaction from `SELECT FOR SHARE`, but does prevent `SELECT FOR UPDATE`, `UPDATE`, `DELETE`.

![[Row-level locks.png]]