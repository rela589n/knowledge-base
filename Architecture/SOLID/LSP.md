---
aliases:
  - Liskov substitution principle
---
Classes that use objects of base classes should not bother themselves with particular implementations (there should not be `instanceof` checks). 

Also, each particular implementation must follow the interface it implements without breaking it (input parameters must be the same type or wider than interface, output parameters (return values) must be the same or narrower than interface). 

Example of violation is when interface declares count to be returned zero or positive, while implementation could return negative values, thereby violating the interface.

