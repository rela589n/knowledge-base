**Hash index** is just a **hash map**, which stores **position of data on the disk**. 

[[Riak]]'s default storage engine for _BitCask_ has great performance for both reads and writes. **Writes** are done to a **log file**, and **reads** use an **in-memory hash-map** containing locations of the data.

This approach is well suited for **intensive writes**.
Reads demand that **all key hashes** must **fit into RAM**.

Since values are always appended to database, the **disk space issue** may arise. Solution for running out of disk space problem:

**Break the log into segment files** such that when current segment overlaps some limit, new segment file is started. 
Hence, **committed segments may be compacted** without locking write operations. 

> **Compaction** - removing duplicated keys and saving only latest value for each particular key.

Moreover, as a lot of keys may be thrown away during segment compaction, it is possible to **merge multiple segments into single**, doing compaction of values at the same time.

**Existing segments are never modified**, hence **merging is done in background**, and it doesn't lock neither read nor write operations. When merge finished, final segment will replace ones it was built upon.

Each segment maintain it's own in-memory hash-map. Not a lot fo segments should exist in order for lookup to be quick.

Real implementation has to handle those issues:
- **File format**. The text files like CSV or similar have overhead for escaping. The best fit here is **binary log file**. Format is such: length of data in bytes followed by this data;
- **Deletion**. In order to delete records, **tombstone record** is created;
- **Crash Recovery**. Reloading all the hash maps into memory on server restart may take a lot of time. Some implementations **do snapshots of each map** on disk;
- **Partially written records**. Writes log file contains each record **checksum** in order to detect and ignore corrupted parts;
- **Concurrency control**. As log is sequential append-only, **writes** are done **in single thread**. While **reads may be concurrent**;

Such design has pros:
- **append-only** is usually **faster than random write**;
- **append-only** makes **crash recovery easier** - no need to handle case when only part of old data was overwritten;
- **merging old segments prevents** problem of **fragmented files** over time.

And cones:
- hash **table must fit into memory**;
- **range queries not supported** (i.e. all keys from kitty00000 to kitty99999).
