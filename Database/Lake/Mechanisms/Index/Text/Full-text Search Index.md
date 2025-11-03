---
aliases:
  - Fuzzy and Full-text Search Indexes
---
[[Full Text Search]] [[Database Index|Index]]. 

Full text search allows use of synonyms in order to ignore grammatical variations. Also, typos tolerance within given edit distance is allowed.

> Edit distance - number of single character changes (add, remove, replace) for original word to make up final word.

*Lucene* uses similar structure to [[SSTable|SSTables]] in order to store terms dictionary. But in-memory index is somewhat different, because it doesn't have the keys itself, but rather finite state automation (kind of _trie_), which can be transformed into _Levenshtein automation_, allowing to search words within given edit distance.

Other fuzzy search go into direction of document classification and ML.
