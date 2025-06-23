Holy Grail of [[Model-driven Design]] is [[Declarative]] Design.
When you define [[Domain Model|Model]] properties, and the rest of the code that is needed to work is organized via reflection, or generated, or what not.

In practice, it's fraught with problems due to the limitations of the frameworks, that doesn't allow to express some specifics of the [[Domain Model|Model]].

Everyone must follow the rules of the framework in order to get the [[Declarative]] design. Thereby, it might be corrupted if bypassed.

**The greatest value** is fine-grained libraries specialized at some particular thing (like [[ORM]]). It relieves from drudge work, leaving freedom in design (yet within limits).

[[Domain-specific Language]]