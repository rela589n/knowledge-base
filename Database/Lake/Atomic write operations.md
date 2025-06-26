In some cases **instead of [[Read-Modify-Write]]**, **atomic modification** may be **applied** to the value, resulting in the final expected state. For instance, increment is applied `SET val = val + 1` , for json modification `jsonb_set` may be used.

This will work correctly, since [[Dirty Write#^1048c2|writes are queued up]] (locked) for all transactions, thus modifications will happen sequentially.
