---
aliases:
  - ISP
---
**Interface Segregation** - methods of the interface must be used together.

***Don't*** force clients to ***implement***  methods they **don't need**. 

Related to [[High Cohesion & Low Coupling|High Cohesion]].
Similar to [[Common Reuse Principle]] .

> **For example**, 
> Client code **implements** the interface.
> There are a lot of **methods we *don't use***, 
> that's a sign that interface is overloaded and should be segregated.
