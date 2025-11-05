**Clocks** are used to:
- *measure* **duration** (e.g. request-response)
- *describe* **points *in* time** (e.g. created_at field, scheduled email).

In [[Distributed System|Distributed Systems]]  it's **hard *to tell***
	*whether* **one event *occured* *before* another**, because of:
- **[[Network Unbounded Delay|Network Delays]]**;
- each **node** *has* its **own clock**.

Every computer has **two physical clocks**:
- [[Wall-Clock|Time-of-day Clock]]; ![[Wall-Clock#^69c3a4]]
- [[Monotonic Clock]]. ![[Monotonic Clock#^4b7ce2]]
There's an issue with any clock check that is related to [[Process Pauses]].