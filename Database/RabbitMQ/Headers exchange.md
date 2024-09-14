This type of exchange completely ignores the routing key.
Routing is implemented exclusively on message headers.

Hence, message should have headers dictionary.
Also, queues are bound to the exchange based on headers.

For example, `rpc` exchange could be bound to:
- `vacation_create_rpc` based on two headers: `{class: vacation, operation: create}`.

In this example, if we try to send a message with headers `{class: vacation, operation: create}`, - it would be delivered to `vacation_create_rpc` queue.

On the other hand, sending `{class: vacation, operation: revoke}` won't deliver it to `vacation_create_rpc`, but could be delivered to `vacatino_revoke_rpc` instead.

