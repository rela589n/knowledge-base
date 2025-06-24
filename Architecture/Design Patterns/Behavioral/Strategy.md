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

Introducing [[Strategy]] by extracting common `interface` for multiple implementations **reduces conceptual [[Coupling]]**, since we can depend only on one `interface` rather than on each concrete implementation. ^d7fee7

Not using Strategy would increase complexity in the client code, because it'd be responsible of all that each particular previously substitutable Strategy does as well as for the process control.
