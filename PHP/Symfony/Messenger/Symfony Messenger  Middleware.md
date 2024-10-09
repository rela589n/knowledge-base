
Each bus has attached middleware by default. This is useful for instance, to wrap handling logic into a transaction (`doctrine_transaction`). 
Default middleware:
- `add_bus_name_to_stamp_middleware` - adds bus name to stamp;
- `dispatch_after_current_bus` - handles logic of dispatching marked messages after current bus success;
- `failed_message_processing_middleware` - processess retried messages as if they were sent to the original transport;
- custom middleware chain;
- `send_message` - sends message to the transport, interrupts chain;
- `handle_message` - calls message handlers.

Middleware is called both on dispatching message to the transport and when receiving message in consumers.

### Handling new messages after handling is done

When message **handler dispatches new messages** (like `UserRegistered` event) we may want to finish current message handlers and middlewares, because if `doctrine_transaction` is used, then email will be sent in `UserRegistered` handlers, while transaction is rolled back later on.

To mark message to be handled after current bus, `DispatchAfterCurrentBusStamp` is used.

```php
$bus->dispatch($event, [new DispatchAfterCurrentBusStamp()]);
```

### Middleware for Doctrine

- `doctrine_transaction` - no need to call `flush()`, error will lead to transaction rollback;
- `doctrine_ping_connection` - check if connection is open, reconnect if needed (useful for long-running workers);
- `doctrine_close_connection` - after handling, closes doctrine connection (useful for long-runnning workers).

### Other middleware

`router_context` - saves request information, which may be used later on for URLs generation.
`validation` - runs the validation of message before processing it (`ValidationFailedException` is thrown if message not valid).
