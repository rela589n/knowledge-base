
Direct exchange - the exchange, that will send the incoming message only to the queues that are bound by the routing key.

For example, `auth_events` exchange could have these bindings:
- `vacation_incoming_events` queue by `user.deleted` key;
- `inventory_incoming_events` by `user.registered` key;
  `inventory_incoming_events` by `user.deleted` key;

It is possible to have multiple bindings.

See [[Symfony Messenger route to different queues]]