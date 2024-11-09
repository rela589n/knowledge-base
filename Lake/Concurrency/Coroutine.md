This is a lightweight non-preemptive thread that doesn't require OS management.

Basically, coroutines switch when currently active coroutine becomes blocked by I/O operation.

![[Coroutine flow.png]]