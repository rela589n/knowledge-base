---
aliases:
  - Master
---
[[K8s Nodes|Node]], responsible for managing the processes of a [[Cluster]].

Every Master Node must have:
- [[Api Server]]
- [[Scheduler]]
- [[Controller Manager]]
- [[etcd]]

To be reliable, [[Cluster]] must have at least **two Mater Nodes**.
