---
aliases:
  - Modularity
  - Modules
---
Module is a selection of objects based on their [[Domain Model|Domain Meaning]]; Module groups set of concepts with [[High Cohesion & Low Coupling|High Cohesion]].

Модуль - это **набор классов**, которые являют собой **единое целое**.
В случае модуля, состоящего из нескольких классов, то эти классы **не могут существовать** один **без другого**. 

> К примеру, **Questionnaire** не может существовать без **QuestionnaireSection**, который, в свою очередь, не может существовать без **QuestionnaireQuestion**. 
> Обратная цепочка также верна. 
> Таким образом, всё это составляет единый модуль - Questionnaire, который также содержит в себе подмодули.

Primary aim for [[Module|Modularity]] is **reduced cognitive load**, since there's a limited number of things we could think about at once.

Modules should tell the [[Cohesion|Cohesive]] story of the system, resulting in **conceptual clarity**.

[[Module|Modularity]] contributes to [[Ubiquitous Language]], and provides a good separation for the **means of communication**.

Most reasonable basis of the module is [[Aggregate]].

Every module must be possible to be understood with minimum number of references to other modules ([[High Cohesion & Low Coupling|Low Coupling]]).

> If your [[Domain Model|Model]] is telling a story, your [[Module]] is a chapter.

See also [[Folder by type packaging]]
