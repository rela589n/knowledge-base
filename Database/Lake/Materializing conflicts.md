**Materializing conflicts** - **last resort** approach to **prevent [[Solutions to write skew|write skew]]** when **write depends on absence of rows**. The **separate table** is introduced, which is not used for storing the actual information, but rather it is **used as a collection of locks**. **Read query will lock respective rows** in this table and other transaction which overlaps with current one will have to wait.

Considering meeting room booking example, table will contain data with 15 minutes time slots for every room for next 6 months. The transaction will lock overlapping rows in this table.

This approach is a **Last Resort**, usually **[[Serializable|Serializability]] should be used instead**.