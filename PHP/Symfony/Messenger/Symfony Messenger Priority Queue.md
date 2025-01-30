[[Symfony Messanger]]

```yaml
framework:
  messenger:
    transports:
      async_authentication:
        dsn: '%env(MESSENGER_TRANSPORT_DSN)%'
        options:
          auto_setup: true
          exchange:
            name: authentication
          queues:
            messages_authentication:
              arguments:
                # https://www.rabbitmq.com/docs/priority
                x-max-priority: 5
```

This will create priority queue with `x-max-priority: 5`.

Then, in order to dispatch message with particular priority, use `AmqpStamp`:

```php
public function dispatch(Uuid $id): void
{
    $command = new SendWelcomeEmail($id);

    // Using the lowest priority, as the same consumer is used for other more needed purposes
    $amqpStamp = new AmqpStamp(attributes: ['priority' => 1]);

    $this->consumerBus->dispatch($command, [$amqpStamp]);
}
```

Then, consuming messages is really simple:

```shell
bin/console messenger:consume async_authentication -vv --memory-limit=128M --time-limit=3600
```
