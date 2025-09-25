---
aliases:
  - POD
---
**POD** is an abstraction over **[[Container]]**, the smallest unit in [[Kubernetes|K8s]]. 
Usually runs **one app [[Container]]** inside (could be with supplement).

POD can be used for:
- database
- application ([[PHP-FPM]]+[[Nginx]] / [[RoadRunner]])
- consumers

[[Kubernetes|K8s]] offers virtual **network**. Each **POD** gets a unique **IP address**. 
When **POD dies**, a **new IP address** will be used for the new Pod.

Static address can be achieved with a [[Environments/Kubernetes/Components/Service/Service|Service]].

You don't create PODs manually. You create [[Deployment]]s.
