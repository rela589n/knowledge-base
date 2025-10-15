**SAGA** provides **[[Transaction]] management for [[Microservices]]**, 
or any place where single [[Transaction|DB Transaction]] can't be used.

SAGA *consists of* **multiple steps**, 
	*each is* a **local transaction** 
		([[Transaction]] performed by particular [[Microservices|Microservice]]), 
	*executed* **in order**.

It **guarantees**:
	*either* **all** transactions **complete** successfully, 
	*or* series of **compensations** are **executed** in case of failure.

There are two **ways of implementing** SAGA:
- [[Choreography SAGA]]
- [[Orchestrator SAGA]]

Transactions can be *reverted by* **compensating transactions**.

![[Booking SAGA Flow.png]]

Sometimes it can happen that 
	calling side regards Action as failed, 
		but the Action itself thinks to have succeeded 
		(or at least could have polluted the state during failure). 
In this case, it makes sense
	to include [[SAGA]] compensations 
		before the respective Actions are executed 
	so that such "partial success" Actions will be rolled back.
	