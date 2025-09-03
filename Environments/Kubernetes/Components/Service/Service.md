---
aliases:
  - Service
---
**Service** is an abstraction over [[POD]] (type of the [[POD]]s group) that guarantees that even though the **[[POD]] dies**, a **new** one will be **created**.
Service offers a **static IP address**. 

Similar to [[Docker Compose]] Service.

Services can be:
- [[Internal Service|Internal]];
- [[External Service|External]].

![[K8s.png|330]]

Service also acts as a [[Load Balancer]] - forwards request to the least busy [[POD]].

![[Service Load Balancing.png|500]]
