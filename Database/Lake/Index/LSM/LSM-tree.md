**LSM** stands for **Log-Structured Merge-Tree**.

### Making an LSM-tree of SSTables

LSM storage engines are based on this principle of merging and compacting sorted files.

Lucene (indexing engine used by [[ElasticSearch]] and Solr) uses similar method for storing its _term dictionary_. The mappings from terms to postings list is kept in SSTable-like files, which are merged when needed.

##### Performance Optimizations

LSM-tree algorithm may be slow when looking for keys, which are not present in database.  It requires to check all segments in their order. This kind of acces is optimized by _Bloom filters_ - data structure for approximating the contents of a set. It can tell if key doesn't exist using bitmasks.

Another topics are strategies how to compact and merge SSTables. Most common are:
- size-tiered ([[HBase]], [[Cassandra]]);
- leveled ([[LevelDB]], [[RocksDB]], [[Cassandra]]).

Size-tiered strategy successively merges newest (and smallest) SSTables into oldest (and largest) ones.
Leveled strategy requires less disk space and makes more incremental compaction.

> LSM-trees allow range queries (scan for keys from L unto R)
