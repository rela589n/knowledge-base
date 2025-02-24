When we need to pass the data in one format into the class that accepts it in another.
 
Example: 
- flysystem adapters (we have common interface, behind which each particular adapter does the needed job).
- symfony cache component (`FilesystemAdapter`, `RedisAdapter`, `MemcachedAdapter`)
- symfony messenger transports (`AmqpTransport`, `SqsTransport`, `DoctrineTransport`)
- custom email adapter 
- DI-box (from unbalanced jack to balanced xlr)
