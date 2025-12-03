---
aliases:
  - Chain of Command
---
**Chain of Responsibility** - ***pass* the request** through the **chain of handlers**. Each **handler *decides*** what to do with it
(either to **process** is or **pass through** to the next handler).

**Example:**
- **Laravel's middleware**
- Symfony's **message bus** middlewares:
	- `RejectRedeliveredMessageMiddleware` (sf middleware)
- Symfony **event listeners** with **stop** propagation.
