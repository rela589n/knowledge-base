Commit order should be following:
- deletions
- insertions
- updates

Deletions must come first ([[Entity deletion happens last]] in [[Doctrine ORM]]), because we could just replace the entity with a new one.

Yet, this is not always the case.

Say, we have entity A that has foreign_b column. And we have entity B.


| Entity A | id  | foreign_b |
| -------- | --- | --------- |
|          | 1   | 2         |
|          | 2   | 3         |

| Entity B | id  |
| -------- | --- |
|          | 2   |
|          | 3   |
|          | 4   |

In this case, if we replace 3 with 5, then we have to:
- insert new record B5
- update the existing A2
- delete old B3
