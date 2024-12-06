```yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true
        bind:
        
            $smsGateway: '@=env("SMS_PROVIDER") == "turbo_sms" ? service("App\\TurboSmsGateway") : service("App\\StubSmsGateway")'
```

