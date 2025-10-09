[[B-Tree]] vs [[LSM-tree]]

### Comparing B-Trees and LSM-trees

Generally it is considered that **[[B-Tree]]s** are **faster** for **read**, 
while **[[LSM-tree]]s** are **faster** for **write**. 

Besides that, **[[B-Tree]]s** are more **mature** and widely used.

#### Advantages of LSM-trees

B-tree storage engine must write data at least twice: to [[Write-Ahead Log|WAL]] and to the index itself. And probably once more when page split is required (on overflow).

Log-structured indices have to do some additional job (compaction and merging of segments). When one incoming write to DB produces multiple writes to disk over DB lifetime is called _write amplification_. 

LSM-trees typically have higher write throughput than B-trees partly because sometimes write amplification is lower, and partly because they are not page-oriented, and don't have to overwrite the whole page on disk when few bytes were updated, but instead write compact SSTables sequentially.

LSM-trees are compressed better. No fragmentation is possible with LSM-trees, hence it takes less storage overhead (especially with leveled compaction).

On SSD, lover _write amplification_ and absense of fragmentation is beneficial: it allows more writes and reads within available I/O bandwidth.

#### Downsides of LSM-trees

The background merge of segments may interfere with incoming reads/writes. Even though, conceptually two are independent, they still use same shared resource - disk. Disks have limited resources, which means that some request will need to __wait until__ disk __finishes__ expensive __compaction__ operation. The impact is visible at hight percentiles.

When write throughput is high, the background compaction may not keep up with incoming writes. This slows down both write and read throughput, because the incoming writes share disk write bandwith with background process, and reads have to check a lot of segments to find value. The higher database gets, the bigger disk bandwidth is required for compaction.

The advantage of B-tree is that any particular key may exist only in single place of database. It offers ease of implementation of transactional processing, which is usually implemented using locks on keys ranges. Locks may be attached directly to tree.

> It is better to test workload empirically on different storage engines to choose the best.
