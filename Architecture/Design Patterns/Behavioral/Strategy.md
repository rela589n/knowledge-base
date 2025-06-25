---
aliases:
  - Policy
---
**Strategy** [[Encapsulation|Encapsulates]] the **varying part of the process**. 
Used when there are **multiple algorithms** (family of algorithms) that are **used [[Polymorphism|Polymorphically]]** , and **selected at runtime**.

> Each [[Strategy]] represents one **way of doing the action**.

![[Strategy.png]]

Example:
- id generation strategy
- orm hydration mode (hydrate array, hydrate object);
- payment method (credit card, internal currency, cash on delivery);
- question activation strategy.

Introducing [[Strategy]] by extracting common `interface` for multiple implementations **reduces conceptual [[Coupling]]**, since we can depend only on one `interface` rather than on each concrete implementation. ^d7fee7

Not using [[Strategy]] would increase complexity for the client code, since it'd be responsible for all that each particular otherwise [[Polymorphism|Substitutable]] Strategy would've represented as well as for the process control itself.

