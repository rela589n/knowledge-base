---
aliases:
  - Adapters
---
**Adapter** adapts **third-party interface** to the **client interface**.

It allows **client to use known interface**, and [[Adapter]] will convert passed parameters for the interface of the adapted system.
 
Example: 
- [[Anti-Corruption Layer]]
- flysystem adapters (we have common interface, behind which each particular adapter does the needed job).
- symfony cache component (`FilesystemAdapter`, `RedisAdapter`, `MemcachedAdapter`)
- symfony messenger transports (`AmqpTransport`, `SqsTransport`, `DoctrineTransport`)
- custom email adapter 
- DI-box (from unbalanced jack to balanced xlr)
