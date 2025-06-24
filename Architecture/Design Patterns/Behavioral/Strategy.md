---
aliases:
  - Policy
---
**Strategy** [[Encapsulation|Encapsulates]] the varying part of the process. 
Used when there are **multiple algorithms** (family of algorithms) that must be **used polymorphically** in different scenarios, and particular **algorithm is selected at runtime**.

![[Strategy.png]]

Example:
- id generation strategy
- orm hydration mode (hydrate array, hydrate object)
- payment method (credit card, btc card, cash on delivery)
- question activation strategy

Not using Strategy would increase complexity in the client code, because it'd be responsible of all that each particular Strategy does as well as for the process control.
