```yaml
App\Gateway\SmsGateway:
    factory: '@=env("SMS_PROVIDER") == "turbo_sms" ? service("App\\Gateway\\TurboSmsGateway") : service("App\\Gateway\\StubSendSmsGateway")'
```
