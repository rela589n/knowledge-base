**Read Committed** - [[Transaction Isolation Level|Isolation Level]] that provides the following guarantees:
- **[[Dirty Read#^d421eb|NO Dirty Reads]]** (***read*** only **what's committed**);
- **[[Dirty Write#^1048c2|NO Dirty Writes]]** (***overwrite*** only **what's committed**).

It doesn't prevent [[Lost Update]] in [[Read-Modify-Write]] cycle.
