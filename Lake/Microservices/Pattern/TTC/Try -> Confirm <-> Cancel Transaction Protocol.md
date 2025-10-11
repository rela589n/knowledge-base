---
docs:
  - https://docs.oracle.com/en/database/oracle/transaction-manager-for-microservices/24.2/tmmdg/tcc-transaction-model.html
aliases:
  - TTC
---
**Try - Confirm/Cancel (TTC)** is based on the idea of **reservations**.

It's **similar to** manually implemented **[[Two-phase commit|2PC]]**, where:
- the first **(Try) phase** is making change to **reserve**;
- the second **(Confirm/Cancel) phase** is either:
	- **confirm** the reservation;
	- **cancel** the reservation.

Yet, it's **different** *from* **[[Two-phase commit|2PC]]** because it's 
**[[Microservices|Microservice]] itself** that *initiates* **reservations**.

If something goes wrong **after Try phase**, it's all 
automatically canceled after **reservation timeout**.

![[TTC Protocol.png]]