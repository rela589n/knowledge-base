**RD-[[B-Tree|Tree]]** (Russian Doll [[B-Tree|Tree]]) - a variation of [[R-Tree]] that organizes data into a generalized **[[Balanced Tree|Tree]] of bounded [[Set|Sets]]**.

Each intermediary node has a **bounding set**,
which is a <b><u>union set</u> <i>of</i></b> all **children's keys**.

For example, search terms set:
![[RD-Tree.png]]

The higher to the root, the larger is the index row.
As an optimization, [[Signature Tree]] is used.

See [docs](https://dsf.berkeley.edu/papers/UW-CS-TR-1252.pdf)

