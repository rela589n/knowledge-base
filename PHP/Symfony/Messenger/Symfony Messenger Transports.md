
By default, each message is dispatched to the handlers right away (sync). Though, it is possible to define transports for particular messages in order to pass them to the queue and process in async manner.

## Workers (consuming the messages)

The command to consume the message:

`messanger:consume <transport>`

When the message is consumed **all handlers for this message are called**. Though, if message was delivered to multiple transports, we may want to limit handlers to some specific transport.

The `fromTransport` is responsible for binding handler to the specific transport.
