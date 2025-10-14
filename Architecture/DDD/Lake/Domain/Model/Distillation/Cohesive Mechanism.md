---
aliases:
  - Coherent Mechanism
---
**[[Cohesion|Cohesive]] Mechanism** - a part that *[[Encapsulation|Encapsulates]]* **complex algorithm** *behind* **simple [[Intention-Revealing Interface]]**.

> **Example**: [[Specification]].

Allows **client [[Subdomain|Component]]** to *use* **simple [[Declarative]] [[Intention-Revealing Interface|Interface]]**
	(state the [[Business Rule|Rule]]), 
*while* your **[[Cohesive Mechanism]]**  **implements it**
	(resolve the [[Business Rule|Rule]]).

It makes **main [[Subdomain|Component]]** ***easier to* [[Comprehension|Understand]]**.

Keeping it **separate from** the main **[[Domain Model|Model]]** is good 
due to **[[Low Coupling & High Cohesion|Low Coupling]]**:
- easier to use **another** option;
- easier to **[[Testing|Test]]**.

**Most useful** when used with **[[Flexible Design|Supple Design]]**.

It's **not** a **[[Generic Subdomain]]** as it 
does **not** hold any **[[Ubiquitous Language|Domain Knowledge]]**.

Draw on [[Established Formalisms|Established Formalisms]] to have [[Comprehension|Familiar]] terminology.
It should have a **bare minimum** of what's needed, not fully-grown [[Domain Model|Model]].