---
aliases:
  - ISP
---
**Interface Segregation** - clients should **not** be **forced to implement** the interfaces they **don't need** / **don't use**. 

Related to [[Low Coupling & High Cohesion|High Cohesion]]. Similar to [[Common Reuse Principle]] .

For example, when client code **implements** the interface, if there are a lot of **methods we don't need**, - that's likely that interface is overloaded and should be segregated.
