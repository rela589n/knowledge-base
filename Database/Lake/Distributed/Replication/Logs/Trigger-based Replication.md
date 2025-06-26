The most flexible [[Replication Strategies|Replication Strategy]], though it has the most overhead. It uses **triggers and stored procedures**.  Databus for [[Oracle]] and [[Bucardo]] for [[PostgreSQL]] works this way.

May be useful in case when it's necessary to **[[Replication|Replicate]] only the part of the data** or if **custom conflict resolution logic** is necessary (or any other **custom things**).

When event happens, *trigger* may **write the changes to the separate table**, which is being **listened to by our application** and processed thereafter.
