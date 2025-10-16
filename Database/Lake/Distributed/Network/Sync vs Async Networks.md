![[Sync networks#^3ba1a2]]

![[Async Networks#^07b634]]

If we'd try to send the **bursty traffic via sync net** in order to gain [[Network Bounded Delay]], it would mean we have to guess necessary bandwidth size, while other available **remaining capacity is unused**. 

Async nets dynamically adapt to traffic size, which leads to [[Network Unbounded Delay]].

It requires careful use of **quality of service** (prioritizing packets) and **admission control** (rate-limiting senders) to make [[Async Networks]] **delays bounded enough**. 

Though, public clouds and multi-tenant datacenters do not enable it, therefore we have **no network guarantees**.