Happens when [[Temporal/Workflow/Workflow|Workflow]] executes for longer time (see [RPC timeout](https://docs.temporal.io/develop/php/temporal-clients#configure-rpc-timeout)) than [[Client]] is intended to wait. 

In this case `Temporal\Exception\Client\TimeoutException` is thrown.

Actually message "Deadline Exceeded" can be somewhat misleading. You can configure custom "timeout" (`withTimeout()` method) and "deadline".

If you are using [[Vanta Bundle]], you can set it in the config:

```diff
clients:
    default:
        namespace: default
        address: '%env(TEMPORAL_ADDRESS)%'
        dataConverter: temporal.data_converter
+       grpcContext:
+           timeout:
+               value: 10
```