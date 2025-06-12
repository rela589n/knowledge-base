---
developed-by: Evans, Fowler
---
> Some [[Domain|Business]] rules (those including lots of conditions) could not find their place in any [[Entity]] or [[Value Object]]. They deserve a designated [[Specification]] object.

**Specification** is a [[Predicate]]-like object that encapsulates the algorithms of verifying whether the object satisfies the criteria. It defines **"what it means to be `<adjective>`"**, and it can evaluate it for candidate.

[[Specification]] is suitable for these use-cases:
- Test if object fulfills some need / suitable for smth;
- Select particular object from collection / storage;
- Create new object to fit some need.

> If [[Specification]] needs some external things to check the condition, [[Factory]] could be used to create it.

[[Specification]] allows the client to specify "what" he wants without him being concerned about "how".

**Examples** of [[Specification]]:
- [[Doctrine Criteria]];
- Filters (method `apply()`).
