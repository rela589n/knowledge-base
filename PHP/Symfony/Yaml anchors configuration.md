```yaml
when@dev: &transport
    framework:
        messenger:
            routing:
                App\YourCommand: sync

when@test: *transport
```

```yaml
when@stage:
    services: &foo
        foo:
            class: stdClass

when@dev:
    services:
        <<: *foo
        bar:
            class: stdClass
```