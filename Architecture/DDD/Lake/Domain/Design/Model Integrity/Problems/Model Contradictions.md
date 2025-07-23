---
aliases:
  - Splinters
  - Model Fragmentation
  - Model Contradictions
  - Contradictions
  - Integrity Problems
---
**[[Domain Model|Model]] Contradictions** are **Integrity Problems** that result in **Fragmented [[Domain Model|Model]]**:
- some [[Duplicate Concept|Concepts are Duplicated]] (overcautious devs, or just not realizing it was already there);
- other [[False Cognate|Concepts are Misused]] (they're different)

[[Model Contradictions|Model Fragmentation]]: When [[Bounded Context|Bounded Contexts]] have related [[Domain Model|Models]], it's possible that each develops its own fine-tuned [[Ubiquitous Language|Language]] (like [[Model Unification#^4c61c2|Elephant]]).

It's fraught with:
- loss of [[Ubiquitous Language|Shared Language]] reduces communication;
- overhead of [[Translation Layer|Translation]] during [[Context Integration Map|Integration]];

How valuable is this jargon, peculiar to the [[Bounded Context]]? Sometimes it's just more trouble than it's worth.
