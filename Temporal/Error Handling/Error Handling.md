Categories of failures:
- [[Application Failure]]
- [[Platform Failure]]

Types of failures:
- [[Transient Failure]]
- [[Intermittent Failure]]
- [[Permanent Failure]]

[[Activity|Activities]] should be [[Idempotence|idempotent]], because they are retried.

[[Temporal]] propagates error throw from the code written in one language up to be handled in another language.

![[Multilingual error propagation.png]]
