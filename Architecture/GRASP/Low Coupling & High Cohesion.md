---
aliases:
  - Low Coupling
  - High Cohesion
  - Dependencies
---
Low [[Coupling]] & High [[Cohesion]] used and **work together**:

[[Module|Modules]] and classes must have **least references** in-between so that they can **be understood by themselves** w/o any references.

**Extensive code** with lots of dependencies should **be separated** into **smaller** pieces of code (High [[Cohesion]]), that are least interdependent (Low [[Coupling]]).

High [[Cohesion]] is same [[Single Responsibility Principle|SRP]], [[Common Closure Principle|CCP]], [[Information Expert]] principles.

These concepts play fundamental role at all scales, starting from the big ones like [[Subdomain|Subdomains]], [[Bounded Context|Bounded Contexts]], [[Module|Modules]], and down to [[Aggregate|Aggregates]] and particular classes.
