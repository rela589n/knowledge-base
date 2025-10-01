---
aliases:
  - CI
---
**Continuous Integration** means ***quickly* integrating** all **the work** *within* a [[Bounded Context]] *so that* it's easy to detect and ***quickly* fix [[Model Contradictions]]**.

It **tames [[Model Contradictions|Model Fragmentation]]** and keeps the [[Unified Model|Model Unified]] within the [[Bounded Context]]. Especially valuable when the team increases.

It's is first **about [[Domain Concept|Concepts]]**:
- creating common **[[Ubiquitous Language|Knowledge]]** in the team - **[[Domain Concept|Conceptual]] Integration**:
	- *as* it smoothes the [[Code|Implementation]]
- *and* then it's **about [[Code]]**:
	- frequent **merges**;
	- automatic **tests**.

It's:
- continuous (**frequent**, daily);
- integration (**communicate**, **build, test, merge**).

**Uncoordinated teams** working on closely related features might **go on for a while**, but usually their **work eventually don't match up** and they have to spend time on fixing [[Translation Layer]] that they should've **spent on [[Continuous Integration]]**.

The sooner both teams talk about (and integrate) the changes the better.
