---
aliases:
  - BTree
---
**BTrees** is the structure that keeps **key-value** pairs **sorted by key** (like [[SSTable|SSTables]])
allowing quick lookup and range queries, but use completely different approach from [[SSTable|SSTables]].

BTrees **break the database** down **into [[Page|Pages]]** by 4Kb (or 8Kb) and read/write one [[Page]] at a time.

Each **[[Page]]** has it's **own address**, and one **page may refer** to another pages (like _pointers_).

**Branching Factor** - the **number of references to child pages** from single [[Page]]. Typically it is several hundred.

![[BTree.png]]

On **data lookup** we start from the root [[Page]], and find the **adjacent keys** to the given key. Then we **follow [[Page]] reference**, and repeat **until** we end up on a **leaf [[Page]]**. Then value for the given key is either found or not.

In order to **update value** of the existing key, find the leaf [[Page]], change value, and write the [[Page]] back on disk.

In order to **add value** by new key **find leaf [[Page]]**, and **if there's enough space**, **write** it. Otherwise, **[[Page Split|Split the Page]] up into two** and update parent [[Page]]'s references. Thereby, there should be enough space.

This algorithm ensures that **tree is balanced** (it's height is Log(n)). Usually there are no more than 4 levels of tree.

#### Making BTrees reliable

The idea behind **write** operation is to **overwrite the whole [[Page]]** with new the data. Compared to LSM-trees, rewrite operation is dangerous, especially if it is necessary to rewrite multiple [[Page|Pages]] at once (for example, overfull [[Page Split]] requires write of three pages on disk). If **server crashes** suddenly, there's a chance to get a **corrupted index**. This is resolved with the [[Write-Ahead Log]] used on **failover**.

There is another issue with **concurrency control**, because multiple threads may try to **write same [[Page|Pages]]** at the **same time**. Therefore tree data structures are **protected by latches** (lightweight locks).

#### BTree optimizations

- **instead of [[Write-Ahead Log|WAL]]**, **copy-on-write** approach may be used. **Modified [[Page]]** does not overwrite original one, but is **written to a different location**. Also, new versions of parent pages in tree are created, which point to a new page. Such approach is **useful for concurrency control**;
- for **interior nodes** of a tree we **don't need to save the whole key**, because it is only necessary for the boundary purpose. The more keys we can pack into page, the **higher branching factor**, the less levels tree will have. This is known as **B+tree optimization**;
- though there's no strict requirement about where pages should be located, usually BTree implementations try to **maintain leaf pages sequential** on the disk, because if the **large key scan** will be necessary, **sequential disk read** is more effecient. Though, when DB grow, it is hard to maintain this order;
- **additional pointers** may be added **to the leaf [[Page|Pages]] to it's siblings** to allow **sequential scan** without jumping to parent pages;
- some BTree variants are based on **fractal-trees**, which borrow some ideas from **LSM** in order to **reduce disk seeks**.
