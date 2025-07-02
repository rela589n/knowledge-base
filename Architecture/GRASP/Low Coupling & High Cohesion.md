---
aliases:
  - Low Coupling
  - High Cohesion
---
Low [[Coupling]] & High [[Cohesion]]

There must be **least references** to other [[Module|Modules]] and classes, so that they **can be understood by themselves** w/o any references.

Big code that has a lot of dependencies should be separated into smaller pieces of code (High [[Cohesion]]), that are least interdependent (Low [[Coupling]]).

These concepts play fundamental role at all scales, starting from the big ones like [[Subdomain|Subdomains]], [[Bounded Context|Bounded Contexts]], [[Module|Modules]], and down to [[Aggregate|Aggregates]] and particular classes.
