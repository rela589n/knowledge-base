---
aliases: RR RPC
---

[[RoadRunner]] uses [[Goridge]], that allows us to communicate between GO and PHP.

RPC endpoint is defined this way:

```yaml
rpc:  
    listen: tcp://127.0.0.1:6001
```

RPC allows [[RR server could be reset|to reset RR server]].

Basically, RPC allows to call existing Go functions of [[RR plugins]].

Therefore, to implement custom RPC function, it's necessary to write [[Custom RR plugin]].