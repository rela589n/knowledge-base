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
