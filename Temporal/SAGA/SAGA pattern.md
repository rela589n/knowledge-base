There are two ways implementing saga:
- [[Choreography SAGA]]
- [[Orchestrator SAGA]]

SAGA provides **transaction management for microservices**, or any place where single [[Transactions|DB Transaction]] can't be used.

SAGA consists of multiple steps, each is a local transaction (transaction performed by particular microservice), usually executed in order.

Transactions can be reverted by compensating transactions.

SAGA guarantees that either all transactions complete successfully, or series of compensation transactions are executed in case of failure.

![[Booking SAGA Flow.png]]

