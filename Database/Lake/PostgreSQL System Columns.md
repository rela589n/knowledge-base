`tableoid` - table OID, useful for partitioned tables.

`ctid` (example: 1,4 - page/block number, position on page/block) - physical location of the row within the table. This could be changed after VACUUM operation, and is used only internally. 
