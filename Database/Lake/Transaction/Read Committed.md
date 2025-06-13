**Read committed** - [[Isolation Levels|isolation level]], that provides the following guarantees:
- **[[Dirty Reads#^d421eb|NO Dirty Reads]]** (reads will return **only what was committed**);
- **[[Dirty Writes#^1048c2|NO Dirty Writes]]** (writes will overwrite **only what was committed**).

It doesn't really prevent [[Lost Updates]] in [[read-modify-write]] cycle.