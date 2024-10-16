
By default, each message is dispatched to the handlers right away (sync). Though, it is possible to define transports for particular messages in order to pass them to the queue and process in async manner.


## Workers (consuming the messages)

The command to consume the message:

`messanger:consume <transport>`


