The most flexible way to replicate the data, though it has the most overhead. It uses **triggers and stored procedures**. 

May be useful in case when it's necessary to **replicate only the part of the data** or if **custom conflict resolution logic** is necessary as for any other **custom things**.

When event happens, *trigger* may **write the changes to the separate table**, which is being somehow **processed by our application**. Databus for Oracle and Bucardo for Postgres works like this.
