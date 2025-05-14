There are two ways implementing saga:
- [[Choreography SAGA]]
- [[Orchestrator SAGA]]

SAGA is the pattern that provides transaction management for microservices.

Every step of the SAGA is a local transaction (transaction performed by particular microservice).

Transactions can be reverted by compensating transactions.

SAGA guarantees that either all transactions complete successfully, or series of compensation transactions are executed in case of failure.

![[Booking SAGA Flow.png]]

