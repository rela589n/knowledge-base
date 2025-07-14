---
aliases:
  - Conform
  - Conformity
---
**Conformist** is **one-sided [[Context Integration Strategies|Relationship]]**, in which downstream conforms to upstream's [[Domain Model|Model]]. It's useful for **peripheral extensions** (supportive, ad-hoc) for main system.

**[[Conformist]]** is in a sense similar to [[Shared Kernel]] as the **[[Domain Model|Model]] is the same** (though more replicated, not physically shared). 

**[[Conformist|Conformity]]** enormously **simplifies [[Context Integration Map|Integration]] and [[Model Refinement|Communication]]**, as [[Ubiquitous Language]] is shared with the upstream (who's the driver), it's easy to talk with them.

On the other hand, it completely **restricts the [[Domain Model|Model]]** to the use-cases they have, limiting what's possible.

Typically the **Frontend should [[Conformist|Conform]] the Backend** (yet, being in more close collaboration). In essence, if **system isn't autonomous**, it should [[Conformist|Conform]].

In a sense, writing ad-hoc system with [[Translation Layer]] could result more effort in [[Translation Layer]] than on the application itself.

[[Conformist]] is not [[Customer-Supplier]] relationship. **Downstream is on its own and by itself**.

The **upstream team has no interest** in the downstream team for providing their needs. Downstream can't make it all happen.

There are three **ways out of it** (3rd is [[Conformist|Conforming]]):

(1) Consider **doing without an upstream**. Their value may be overestimated and the dependency cost underestimated.

If **upstream is necessary**, then it all depends on **quality of the abstractions**:

(2) Having **poor upstream** implies the need to **develop own [[Domain Model|Model]]** and implement [[Anti-Corruption Layer]] (complex one), [[Translation Layer|Translating]] their [[Domain Model|Model]] into our [[Domain Model|Model]].

(3) Having a **good upstream**, we should [[Conformist|Conform]] to their [[Domain Model|Model]] without [[Translation Layer|Translation]] or with little adjustments ([[Adapter]]).
