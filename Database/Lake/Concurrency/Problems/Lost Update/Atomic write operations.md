**Atomic write operations** fix [[Lost Update]] problem. 
Similar to [[Serializable]], but on a row-level.

Work correctly as [[Dirty Write#^1048c2|Competing writes are Queued up]] (locked), so that writes only apply sequentially.

Contrary to [[Read-Modify-Write]], it results in the expected state.

For example:
- increment: `SET val = val + 1` ;
- json modification: `jsonb_set`.
