Since **[[Secondary Index|Secondary Indexes]] do not uniquely identify** records, it becomes **complicated** really fast, as we don't know neither **which [[Partition]] to look in** nor where the record is located within the partition.

>> Search servers [[ElasticSearch]], Solr have their main purpose to implement secondary indexes.

Approaches (schemes) to **partition database with secondary indexes**:
- **[[Document-based Secondary Indexes Partitioning|Document-Based]]** partitioning;
- **[[Term-based Secondary Indexes Partitioning|Term-Based]]** partitioning.
