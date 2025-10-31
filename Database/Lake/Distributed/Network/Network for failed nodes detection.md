[[Async Network|Network]] is necessary for **faulty nodes detection**:
- **load balancer** should take **failed node out of rotation**;
- [[5. Replication#Leader failure: failover|failover process]] in distributed single-leader databases.

It is not always possible to tell if node has failed or is it just a network issues, though some cases can define failed node:
- if recepient **host is reachable**, but **port is not open** anymore (process crashed);
- when node **process crashes**, it can quickly **notify other nodes** about crash to prevent them from waiting the timeout;
- **management interface of network switches** may show failed links;
- **Destination Unreachable packet** is sent when **router** is sure that host is unreachable, though it is prone to the net issues itself.

As a fallback option, **[[Network Timeouts|timeout is used]]**, since **node can fail silently**.
