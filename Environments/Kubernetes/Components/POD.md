---
aliases:
  - POD
---
**POD** is an abstraction over **[[Container]]**, the smallest unit in [[Kubernetes|K8s]]. 
Usually runs **one app [[Container]]** inside (could be with suplement).

POD can be used for:
- database
- application ([[PHP]]+[[Nginx]] / [[RoadRunner]])
- consumers

[[Kubernetes|K8s]] offers virtual **network**. Each **POD** gets an **IP address**. 
When **POD dies**, a **new** will have a **new IP address**.
[[Environments/Kubernetes/Components/Service/Service|Service]] is used for the static address.

You don't create PODs manually. You create [[Deployment]]s.
