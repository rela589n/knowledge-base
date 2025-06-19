---
aliases:
  - Linearizable
---
> Concept is similar to [[Serializable|Serializability]] since both definitions include "can be arranged in sequential order", but semantics are different. If DB supports both, it is [[Strict Serializability]].

**Linearizability** (aka **atomic consistency**, **strong consistency**, **external consistency**) - [[Consistency guarantees|consistency guarantee]], which abstracts the system as **if it had only one [[Replication|Replica]]**. In fact, there may be multiple copies, but system looks like as if there were only a single so that app doesn't need to worry about multiple replicas.

Linearizability provides a **recency guarantee**, meaning that once some value was written or read, all **subsequent reads will return latest written value** until it is overwritten again, even though there may be concurrent writes. Once value was actually written, all concurrent reads must return latest value and **not to flip back and forth**.

See [[Linearizability implementations]].


