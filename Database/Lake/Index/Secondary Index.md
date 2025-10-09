**Secondary [[Database Index|Index]]** is stored **outside** of the **main table** space, 
and does **not** necessarily have to be **unique**.

Both [[B-Tree|B-Tree]] and LSM-trees indexes might be used.

There are two ways to **store [[Secondary Index]]**:
- make each **value list** matching **row ids**.
- make each key unique by appending row identifier to it;
