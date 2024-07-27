Messanger allows to separate commands from their handlers. Own services may be implemented using bus.

## Messages and Handlers

The `#AsMessageHandler` attribute is used to define handler autoconfiguration parameters. It is allowed to be put either on class or on method. When put on the class, it has to implement  `__invoke` method and accept message instance.

Each message is just a plain object, which is required to be serializable.

## Dispatching the message

`MessageBusInterface` is used for messages dispatching. The default bus which comes along with symfony is `messenger.default_bus`. Custom bus services are allowed to be defined.

## Transports

By default, each message is dispatched to the handlers right away. Though, it is possible to define transports for particular messages in order to pass them to the queue and process in async manner.

## Workers (consuming the messages)

The command to consume the message:

`messanger:consume <transport>`

When the message is consumed **all handlers for this message are called**. Though, if message was delivered to multiple transports, we may want to limit handlers to some specific transport.

The `fromTransport` is responsible for binding handler to the specific transport.

## Stamps

Stamps hold **additional information** regarding the message. For instance, when using AMQP we may want to delay the message -  this can be accomplished via `DelayStamp`.

Stamps may be added when dispatching messages or via the middleware.

```php
$bus->dispatch(
	new Envelope(
		new SmsNotification('...'),
		[
			new DelayStamp(5000),
		],
	),
);
```


## Middleware

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

