---
aliases:
  - SSTables
---
[[LevelDB]], [[RocksDB]]

**SSTable** is **Sorted String Table** -  data is stored like in segment files, but within each segment all **records** are **sorted by keys**, and there is **no key duplicates** per segment file.

Advantages:
1. **Performant** segments **merge** (with cost of `O(n+m)`).
2. **Not all indexed keys are kept in the hashmap**. The **sparse index** map is kept anyway in memory (one **key per every few kilobytes**). To find a value, adjacent keys present in index are checked, and file is scanned from left pointer until reaching right pointer or until value is found.
3. **Values** may be **grouped in blocks** and **compressed** before writing on the disk since during the read **we scan the file anyway**. Thus every such scan range will be in compressed state in file.

#### Constructing and Maintaining SSTables

Tree data structures allow us to insert values in any order and get them back in sorted order. Insertion is done usually with `O(log(n))` . AVL, Red-Black trees may be used, becuase they imply self-balancing on modification.

To **maintain SSTables** storage engine, there would be necessary:
- when writes comes in, **new value** is **appended to the in-memory tree** (memtable).
- once **memtable is big enough** (few MB), **it's flushed** to the disk. The tree will be written effectively as [[SSTable|SSTables]], because it already maintains order of keys. Every **flush will create a new segment**. During the flush, **new writes** are written **to a new memtable**.
- **to serve the read** requests, first **check the in-memory tree** for given key. If not found, then one by one **check recent segments**.
- **in background** it's necessary to **merge segments** from time to time to discard deleted or overwritten records.
- **for failure-resilience**, when write comes in we can also **write value to the log file**, which will be cleared once [[SSTable|SSTables]] written on disk. This way, **no inserts are lost** when server crashes before memtable gets written to the disk.

> This algo is used in [[LevelDB]], [[RocksDB]]. Similar storage engines are used in [[Cassandra]] and [[HBase]]
