**Signature [[B-Tree|Tree]]** is an optimization of [[RD-Tree]] 
that uses [[Hash Function]] to determine a single true-bit [[Bloom Filter|Filter]] signature.

Used for [[PostgreSQL Full-text]] Indexing.

![[Signature Tree.png]]

Consistency function ensures that all parent nodes bitmask 
cover all their child nodes bitmask.

For [[PostgreSQL]], signatures size is 992 bits.
