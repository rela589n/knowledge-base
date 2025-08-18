At first, you might've assumed that commit order should be following:
- deletions
- insertions
- updates

<s>Deletions must come first</s> ([[Entity deletion happens last]] in [[Doctrine ORM]]), because we could just replace the entity with a new one.

Yet, this is not always the case.

Say, we have entity A that has foreign_b column. And we have entity B.

| Entity A | id    | foreign_b |
| -------- | ----- | --------- |
|          | 1     | 2         |
|          | **2** | **3**     |

| Entity B | id    |
| -------- | ----- |
|          | 2     |
|          | **3** |
|          | 4     |

Normally, if `on-delete = cascade`, we would not like Entity A to be deleted. Instead, we would like to replace B3 with B5. 

In this case we have to:
- insert new record B5
- update the existing A2
- delete old B3

This calls for a graph of Operations to persist the state.