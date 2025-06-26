This is Plain assignment / Rewrite.

**It does "overwrite"** for all these scenarios:
- counter increment ;
- balance changes;
- local change in a complex value, say adding json field ;
- full update of the object (say, two users modify some entity in AP).

This is fraught with [[Lost Update]].

[[Atomic write operations]]