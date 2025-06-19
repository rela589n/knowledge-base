---
aliases:
  - BTree
---
BTrees keep **key-value pairs sorted by key** (alike SSTables) to allow quick lookup and range queries, but use completely different approach.

BTrees **break database** down **into [[Page|Pages]]** by 4Kb and read/write one page at a time.

Each **[[Page]]** has it's **own address**, and one **page may refer** to another pages (like _pointers_).

**Branching Factor** - the **number of references to child pages** from single [[Page]]. Typically it is several hundred.

On **lookup** we start from the root [[Page]], and find the **adjacent keys** to given search key. Then we **follow [[Page]] reference**, and repeat **until** we end up on a **leaf [[Page]]**. Then value is either found or not.

In order to **update value** of existing key, find the leaf [[Page]], change value, and write the [[Page]] back again on disk.

In order to **add value** by new key **find leaf [[Page]]**, and  **write** new value **if there's enough space**. Otherwise, it is **split up into two** and parent [[Page]]'s references are updated. Then there should be enough space.

This algorithm ensures that **tree is balanced** (it's height is Log(n)). Usually there are no more than 4 levels of tree.

#### Making BTrees reliable

Basic idea behind **write** operation is to **overrwrite the whole [[Page]]** content with new data. Compared to LSM-trees, rewrite operation is dangerous, especially if it is necessary to rewrite multiple [[Page|Pages]] at once (for example, overfull [[Page Split]] requires write of three pages on disk). If **server crashes** suddenly, there's a chance to get a **corrupted index**.

To accomplish **failover**, the **write-ahead log** (WAL) is written **before every modification** of BTree. After crash this log is **used to restore DB** to a consistent state.

There is another issue with **concurrency control**, because multiple threads may try to **write same [[Page|Pages]]** at the **same time**. Therefore tree data structures are **protected by latches** (lightweight locks).

#### BTree optimizations

- **instead of WAL**, **copy-on-write** approach may be used. **Modified page** does not overwrite original one, but is **written into different location**. Also, new versions of parent pages in tree are created, which point to a new page. Such approach is **useful for concurrency control**;
- for **interior nodes** of a tree we **don't need to save the whole key**, because it is only necessary for the boundary purpose. The more keys we can pack into page, the **higher branching factor**, the less levels tree will have. This is known as **B+tree optimization**;
- though there's no strict requirement about where pages should be located, usually BTree implementations try to **maintain leaf pages sequential** on the disk, because if the **large key scan** will be necessary, **sequential disk read** is more effecient. Though, when DB grow, it is hard to maintain this order;
- **additional pointers** may be added **to the leaf pages to it's siblings** to allow **sequential scan** without jumping to parent pages;
- some BTree variants are based on **fractal-trees**, which borrow some ideas from **LSM** in order to **reduce disk seeks**.
