---
aliases:
  - Low Coupling
  - High Cohesion
  - Dependencies
---
**High [[Cohesion]]** & **Low [[Coupling]]**

Items must be ***bundled*** to have **least references** in-betwixt 
in order to <i><b>be <u>understood</i> by themselves</u></b> (w/o any references).

Extensive code with lots of dependencies
should **be separated** into **smaller** pieces of Highly [[Cohesion|Cohesive]] code, which is <u>least interdependent</u> (Low [[Coupling]]).

**High [[Cohesion]]** is same [[Single Responsibility Principle|SRP]], [[Common Closure Principle|CCP]], [[Information Expert]] principles.

These play fundamental role at all scales:
- big ones: [[Subdomain|Subdomains]], [[Bounded Context|Bounded Contexts]], [[Module|Modules]];
- and [[Aggregate|Aggregates]] and particular classes.
