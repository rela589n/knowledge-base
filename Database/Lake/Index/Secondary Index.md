**Secondary Index** - index, which does not necessarily have to be unique.

Both [[BTree index|BTree]] and LSM-trees indexes may be used.

There are two ways to store *[[Secondary Index]]*:
- make each key unique by appending row identifier to it;
- make each value list matching row identifiers.
