---
aliases:
  - Conform
  - Conformity
---
**Conformist [[Relationships Between Bounded Contexts|Relationship]]** is applied when full [[Customer-Supplier]] relationship can't be applied, and **downstream is on its own** with what's given.

[[Conformist]] is somewhat similar to [[Shared Kernel]] since [[Domain Model|Model]] is the same (though not physically shared). But with [[Conformist]] the upstream team has no interest in the downstream team.

**Upstream has no intention** for providing downstream needs.

There are three ways out of it.

Consider **doing without upstream**. Their value might be overestimated and the dependency value underestimated.

If upstream **dependency is necessary**, then it all depends on **quality of the abstractions**:

Having **poor upstream** implies the need to **develop own [[Domain Model|Model]]** and implement [[Anti-Corruption Layer]] (complex one), [[Translation Layer|Translating]] their [[Domain Model|Model]] into our [[Domain Model|Model]].

Having a **good upstream**, we should [[Conformist|Conform]] to their [[Domain Model|Model]] without [[Translation Layer|Translation]] or with minor adjustments ([[Adapter]]).

[[Conformist|Conformity]] enormously **simplifies integration and [[Model Refinement|Communication]]** (shared [[Ubiquitous Language]]), and since it's upstream who's driving, this's a good thing to do. 

On the other hand, it completely **binds the [[Domain Model|Model]]** to the use-cases they have, restricting what's possible.

Typically the **Frontend should [[Conformist|Conform]] the Backend** (even though it's more close collaboration). In essence, if **system isn't autonomous**, it should [[Conformist|Conform]].
