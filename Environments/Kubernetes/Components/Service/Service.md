---
aliases:
  - Service
---
**Service** is an abstraction over [[POD]] (type of the [[POD]]s group) that guarantees that even though underneath **[[POD]] dies**, a **new** will be available with the same **static IP address**.

Similar to [[Environments/Docker/Compose/Service|Docker Compose Service]].

Services can be:
- [[Internal Service|Internal]];
- [[External Service|External]].

![[K8s.png|330]]

Service also acts as a [[Load Balancer]] - forwards request to the least busy [[POD]] (my-app) from the available [[Worker Node|Node]]. More in: [[Kube-proxy]]

![[Service Load Balancing.png|500]]
