Index, that can answer query without the need for [[Table Heap|Heap]] access. 

It can be used only when all the requested query columns are stored in the index.

Besides that, each entry must conform [[MVCC Visibility rules]]. It uses Visibility Map to avoid [[Table Heap|Heap]] checks if possible.


