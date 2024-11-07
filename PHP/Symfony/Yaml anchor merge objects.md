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

