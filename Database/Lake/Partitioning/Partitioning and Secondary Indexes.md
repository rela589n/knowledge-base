Since **secondary indexes do not uniquely identify** records, it becomes **complicated** really fast, as we don't know neither **which partition to look** in nor **where record is** located **within the partition**.

>> Search servers ElasticSearch, Solr have their main purpose to implement secondary indexes.

Approaches (schemes) to **partition database with secondary indexes**:
- **[[Document-based Secondary Indexes Partitioning|document-based]]** partitioning;
- **[[Term-based Secondary Indexes Partitioning|term-based]]** partitioning.

