This exchange allows to send the messages to all bound queues.

For example, if there are services interested in all `auth_events`, we could define following bindings:
- `vacation_incoming_events` queue;
- `salary_incoming_events` queue.

This way, whenever user event is dispatched into `auth_events` it will automatically appear in two queues.
