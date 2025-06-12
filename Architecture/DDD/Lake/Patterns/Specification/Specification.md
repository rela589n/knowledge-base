---
developed-by: Evans, Fowler
---
> Some [[Domain|Business]] rules (those including lots of conditions) could not find their place in any [[Entity]] or [[Value Object]]. They deserve a designated [[Specification]] object.

**Specification** is a [[Predicate]]-like object that encapsulates the algorithms of verifying whether the object satisfies this specification criteria. 

[[Specification]] allows the client to specify "what" he wants without him being concerned about "how". 
 
The actual [[Specification]] object usually exposes a method as `isSatisfied(candidate)` to check on the real object.

[[Doctrine Criteria]] is an example of specification.
