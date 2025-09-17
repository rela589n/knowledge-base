---
aliases:
  - Chain of Command
---
**Chain of Responsibility** allows to pass the request through the **chain of handlers**, where each separate **handler decides** what to do with this request (either to **process** is or **pass through** to the next handler).

**Example:**
- **Laravel's middleware** implement CoR pattern
- Symfony's **message bus** middlewares:
	- `RejectRedeliveredMessageMiddleware` (sf middleware)
- Symfony **event listeners** with **stop** propagation.
