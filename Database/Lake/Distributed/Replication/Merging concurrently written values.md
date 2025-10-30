> **Siblings** - values written concurrently.

When it comes to merging the values, **siblings can't be rashly unioned**, because even though we can **easily merge added items**, there would be **issues when deleting items**. 

One sibling may remove the **deleted item from the collection**, while it will still be **kept in another sibling**. To allow deletion, [[Tombstone marker]] can be used.

Usually custom **merging code is error-prone**. The **automatic merge** is possible as well, **using CRDT**s, which merges siblings in sensible way including deletions.
