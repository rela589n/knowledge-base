---
aliases:
  - Idempotent
---
**Idempotent operations** can be **safely** invoked **multiple times** without spoiling state of the application.

**Achieved** with unique **"idempotence key"** 
	that [[Microservices|Service]] accepts as input, 
		and **ignores** the request if **duplicate**.

> **Example**: when we **charge the customer** for particular order, 
> clicking on the **same button** 
> 	triggering two requests 
> shouldn't lead to **double charges**.

Button 1 is not idempotent. Buttons 2 and 3 are idempotent.

![[Idempotence.png|500]]


