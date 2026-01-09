**Signature [[B-Tree|Tree]]** is an optimization of [[RD-Tree]] 
which uses [[Hash Function]] to determine [[Bloom Filter|Filter]] signature -
a single true-bit out of N total size (992 in [[PostgreSQL]]).

Used for [[PostgreSQL Full-text]] Indexing.

![[Signature Tree.png]]

Consistency function ensures that all parent nodes bitmask 
cover all their child nodes bitmask.
