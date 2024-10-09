The `#AsMessageHandler` attribute is used to define handler autoconfiguration parameters. It is allowed to be put either on class or on method. When put on the class, it has to implement  `__invoke` method and accept message instance.

Each message is just a plain object, which is required to be serializable.

## Dispatching the message

`MessageBusInterface` is used for messages dispatching. The default bus which comes along with symfony is `messenger.default_bus`. Custom bus services are allowed to be defined.

When the message is processed **all handlers for this message are called**. 