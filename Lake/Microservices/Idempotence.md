---
aliases:
  - Idempotent
---
**Idempotent operations** can be **safely** invoked **multiple times** without spoiling state of the application.

For example, when we **charge the customer** for particular order, it should be [[Idempotence|Idempotent]] so that multiple requests won't lead to **double charges**.

Button 1 is not idempotent. Buttons 2 and 3 are idempotent.

![[Idempotence.png|500]]
Idempotence is achieved with unique idempotence key that [[Microservices|service]] accepts on input, and ignores the request if it's duplicate.

