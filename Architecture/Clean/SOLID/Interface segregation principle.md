---
aliases:
  - ISP
---
Similar to [[Common Reuse Principle]] - clients should **not be forced to depend** on interfaces they do **not use** / **not implement**. 

For example, when client code **implements** the interface, if there are a lot of **methods we don't need**, - that's likely that interface is overloaded and should be segregated.
