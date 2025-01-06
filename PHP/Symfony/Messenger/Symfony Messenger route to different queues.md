[[Symfony Messanger]]

```yaml
framework:
    messenger:
        transports:
            async_document_sign:
                dsn: '%env(MESSENGER_TRANSPORT_DSN)%'
                options:
                    auto_setup: true
                    exchange:
                        type: direct
                        name: document_sign
                        default_publish_routing_key: default
                    queues:
                        messages_document_sign_document:
                            binding_keys: [ document_sign_document ]
                        messages_document_sign_ack_signature:
                            binding_keys: [ document_sign_ack_signature ]
                        messages_document_sign_ack_third_party:
                            binding_keys: [ document_sign_ack_third_party ]
                        messages_document_sign_default:
                            binding_keys: [ default ]
```


Then dispatch it with `AmqpStamp`:

```php
$this->messageBus->dispatch($command, [
    new DispatchAfterCurrentBusStamp(),
    new AmqpStamp('document_sign_document'),
]);
```

Here, the same key is used with `binding_keys`, and [[RabbitMQ]] will forward that message into the respective queue.

To run the consumer for particular messages only:

```shell
bin/console messenger:consume async_document_sign --queues=messages_document_sign_document --queues=messages_document_sign_ack_signature --queues=messages_document_sign_ack_crm --queues=messages_document_sign_default -vv --memory-limit=128M --time-limit=3600
```

