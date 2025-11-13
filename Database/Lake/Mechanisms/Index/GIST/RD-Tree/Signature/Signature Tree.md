**Signature [[B-Tree|Tree]]** is an optimization of [[RD-Tree]] 
that uses [[Hash Function]] to determine its [[Bloom Filter|Filter]] signature,
which is a single true-bit out of N total size (992 in [[PostgreSQL]]).

Used for [[PostgreSQL Full-text]] Indexing.

![[Signature Tree.png]]

Consistency function ensures that all parent nodes bitmask 
cover all their child nodes bitmask.
