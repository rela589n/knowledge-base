There are two ways implementing SAGA:
- [[Choreography SAGA]]
- [[Orchestrator SAGA]]

SAGA provides **transaction management for microservices**, or any place where single [[Transaction|DB Transaction]] can't be used.

SAGA consists of multiple steps, each is a local transaction (transaction performed by particular microservice), usually executed in order.

Transactions can be reverted by compensating transactions.

SAGA guarantees that either all transactions complete successfully, or series of compensation transactions are executed in case of failure.

![[Booking SAGA Flow.png]]

Sometimes it can be that calling side regards Action as failed, but the Action itself thinks to have succeeded (or at least could have polluted the state during failure). In this case, it makes sense to include [[SAGA]] compensations before the respective Actions are executed so that such "partial success" Actions will be rolled back.