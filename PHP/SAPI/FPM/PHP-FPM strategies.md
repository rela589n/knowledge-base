There are three fpm strategies:
- on-demand
- static
- dynamic

#### On-demand
**On-demand** - initially pool is empty. New processes are created on demand. If there are no incoming requests, - processes are removed after reaching idle_timeout.

> **Proc**: resource-efficient
> **Cons**: It adds additional latency time for creating and terminating the worker.

#### Static
**Static** - a fixed number of processes is maintained. It is required to set max_requests option to sort out memory leaks problem.

> **Proc**: predictable performance
> **Cons**: limited performace

#### Dynamic
**Dynamic** - initially a number of idle workers is created. If there are more workers needed, they are added (up to reaching maximum number of workers).

> **Proc**: favorable combination of static and on-demand strategies

![[Pasted image 20240914203222.png]]