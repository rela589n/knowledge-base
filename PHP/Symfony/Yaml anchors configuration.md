```yaml
when@dev: &transport
    framework:
        messenger:
            routing:
                App\YourCommand: sync

when@test: *transport
```

[[Yaml anchor merge objects]]