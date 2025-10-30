[[Secondary Index]] stores [[Primary Key]], so double index lookup is needed:

![[MySQL Secondary Index.png]]
[[MySQL]] uses an extra layer of indirection: [[Secondary Index]] records point to [[Primary Key|Primary Index]] records, and the [[Primary Key|Primary Index]] itself holds the on-disk row locations. If a row offset changes, only the [[Primary Key|Primary Index]] needs to be updated.
