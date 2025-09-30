---
aliases:
  - Context Mapping
  - Integration
  - Model Map
  - Domain Integration
---
**[[Bounded Context|Context]] Map** is a ***global* view** 
	*of* the **[[Bounded Context|Contexts]]** 
	*and* **[[Context Integration Strategies|Relationships]] between them**. 

It's a **manager's view** of the Design:
- We can *see* the **[[Bounded Context|Contexts]]** and **who's working** on them;
- Useful for **cross-team** *collaboration*.

Each **[[Bounded Context|Context]]** must *have* a **[[Ubiquitous Language|Name]]** *and* **clear [[Bounded Context Boundary|Boundaries]]**.

Direct **[[Code]] reuse** *between [[Bounded Context|Contexts]]* is **prohibited**:
- It's fraught with [[Model Contradictions|Model Fragmentation]] issues.
- ***Instead***, proper **[[Context Integration Strategies|Relationships]]** must be **established**.

To **improve** *the* **existing project**:
- **mark** *the current* **situation** *as it is*, not as we'd like:
	- name [[Bounded Context|Contexts]]
	- define [[Context Integration Strategies|Relationships]]
- improve:
	- [[Continuous Integration]]
	- set up [[Anti-Corruption Layer]]
	- use [[Ubiquitous Language]]

**Contracts** are **touch points** between [[Bounded Context|Bounded Contexts]].
Describe them and their nature explicitly.

When *integrating* **own [[Bounded Context|Bounded Contexts]]**, 
we *have* **more freedom** *than* in case of **[[External Systems Integration|External]]**:
- we can jointly develop **simple [[Translation Layer]]**
  *and* **adjust** both [[Bounded Context|Contexts]]

[[External Systems Integration]]