Easier **to avoid [[Skewed partitioning|skews]]** and [[Hot spot|hot spots]].

Partitioning is **done by range of hashes** of keys **rather than keys** themselves (as in [[Partitioning by Key Range]]). The **hash ranges** can be **evenly spaced** as far as data is evenly distributed by the **hash function**.

## Hash functions

**Hash function** is used to determine the partition for given key. **Built-in functions** `Object.hashCode()` are **not suitable** for partitioning, since hash may differ in different processess.

> >**Consistent hashing** doesn't work well for databases, hence rarely used.

## No range queries

As far as **data is scattered** across the partitions, it is **not possible** to run effecient **range queries**, which are possible when partitioning by key:
- MongoDB sends range query **to all partitions**;
- Voldemort, Riak, Couchbase **do not support**;
- **Cassandra** does the compromise using **concatenated index**. 

## Elegant one-to-many

**Concatenated index approach** - elegant way for **one-to-many** relationships partitioning. The many-side table may declare **composite primary key**. **Partitioning** is done only **by the first column**, which is the owner column. This approach allows us to **effectively scan over the many side** of a relationship.
