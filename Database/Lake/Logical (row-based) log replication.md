The **dedicated log** for replication is used.  Used in MySql.

Log describes enough row-based data to reproduce events:
- for deletion, primary key is written;
- for creation, all columns data is written to the log;
- for updation, all changed columns are written.

Since replication log is decoupled from WAL, it is easy to **use different versions of database** across the nodes, because replication BC is easily achievable. Moreover, it is even possible to use **different storage engines**.

It is also easier for **separate applications to parse the log**. Therefore this data may be sent to the Data Warehouse or to main app in order to build caches/indices/etc. This technique is called **change data capture**.