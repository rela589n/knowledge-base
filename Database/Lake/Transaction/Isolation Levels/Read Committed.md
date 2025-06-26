**Read committed** - [[Transaction Isolation Level]], that provides the following guarantees:
- **[[Dirty Reads#^d421eb|NO Dirty Reads]]** (return **only what was committed**);
- **[[Dirty Write#^1048c2|NO Dirty Writes]]** (overwrite **only what was committed**).

It doesn't prevent [[Lost Update]] in [[Read-Modify-Write]] cycle.
