---
aliases:
  - Conform
  - Conformity
---
**Conformist** is **one-sided [[Model Context Strategies|Relationship]]**, applied when full [[Customer-Supplier]] relationship can't be applied, and **downstream is on its own** with what's given.

[[Conformist]] is somewhat similar to [[Shared Kernel]] since the **[[Domain Model|Model]] is the same** (though not physically shared). 

The **upstream team has no interest** in the downstream team for providing their needs. Downstream can't make it all happen.

There are three **ways out of it** (3rd is [[Conformist|Conforming]]):

(1) Consider **doing without an upstream**. Their value may be overestimated and the dependency cost underestimated.

If **upstream is necessary**, then it all depends on **quality of the abstractions**:

(2) Having **poor upstream** implies the need to **develop own [[Domain Model|Model]]** and implement [[Anti-Corruption Layer]] (complex one), [[Translation Layer|Translating]] their [[Domain Model|Model]] into our [[Domain Model|Model]].

(3) Having a **good upstream**, we should [[Conformist|Conform]] to their [[Domain Model|Model]] without [[Translation Layer|Translation]] or with minor adjustments ([[Adapter]]).

**[[Conformist|Conformity]]** enormously **simplifies Integration and [[Model Refinement|Communication]]**, as [[Ubiquitous Language]] is shared with the upstream (who's driver), it's easy to talk with them.

On the other hand, it completely **restricts the [[Domain Model|Model]]** to the use-cases they have, limiting what's possible.

Typically the **Frontend should [[Conformist|Conform]] the Backend** (though it's more close collaboration). In essence, if **system isn't autonomous**, it should [[Conformist|Conform]].
