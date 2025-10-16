In some cases **instead of [[Read-Modify-Write]]**, one may ***apply*** **atomic modification** to the value, resulting in the final expected state. 

For example:
- increment with `SET val = val + 1` ;
- make json modification using `jsonb_set`.

It will work correctly, since [[Dirty Write#^1048c2|writes are queued up]] (locked) for all [[Transaction|Transactions]], therefore modifications only happen sequentially.
