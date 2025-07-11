---
aliases:
  - Adapters
---
**Adapter** allows client to use implementation, adapted to the interface that client understands.

We pass the parameters in **one format**, and **adapter adjusts** it for the interface accepting **another**.
 
Example: 
- [[Anti-Corruption Layer]]
- flysystem adapters (we have common interface, behind which each particular adapter does the needed job).
- symfony cache component (`FilesystemAdapter`, `RedisAdapter`, `MemcachedAdapter`)
- symfony messenger transports (`AmqpTransport`, `SqsTransport`, `DoctrineTransport`)
- custom email adapter 
- DI-box (from unbalanced jack to balanced xlr)
