`services.yaml` configuration file:

```yaml
services:
  routable.event.bus:
    class: Symfony\Component\Messenger\RoutableMessageBus
    arguments:
      - !tagged_locator { tag: 'messenger.bus', index_by: 'id' }
      - '@event.bus'
```
