---
aliases:
  - Adapters
---
**Adapter** adapts **external interface** into the **client interface**.

**Client** uses **known interface**, and [[Adapter]] **converts parameters** into semantically equivalent parameters of adapted interface, 
and **interpret produced results** in terms of our interface.

Example:
- [[Anti-Corruption Layer]]
- **flysystem** adapters (we have common interface, behind which each particular adapter does the needed job).
- symfony **cache adapters**: (`FilesystemAdapter`, `RedisAdapter`, `MemcachedAdapter`)
- symfony **messenger transports** (`AmqpTransport`, `SqsTransport`, `DoctrineTransport`)
- custom **email adapter**
- DI-box (from unbalanced jack to balanced xlr)
