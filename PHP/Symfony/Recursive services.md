The key idea is using `!service_locator` for the sake of factory, making the real service (non-stack) instance lazy.

`phd_exceptional_validation.exception_unwrapper` - the service (lazy) that is going to be used in the main code.

`phd_exceptional_validation.exception_unwrapper.stack` - the starting service other decorators will stack on.

`phd_exceptional_validation.messenger.exception_unwrapper` - the recursive service (accepts inner unwrapper service as `'@.inner'` and outer unwrapper service as `'@phd_exceptional_validation.exception_unwrapper'`)

```yaml
    phd_exceptional_validation.exception_unwrapper:
        public: true
        class: PhPhD\ExceptionalValidation\Unwrapper\ExceptionUnwrapper
        factory:
            - !service_locator
                stack: '@phd_exceptional_validation.exception_unwrapper.stack'
            - get
        arguments: [ stack ]
        lazy: true

    phd_exceptional_validation.exception_unwrapper.stack:
        class: PhPhD\ExceptionalValidation\Unwrapper\PassThroughExceptionUnwrapper

    phd_exceptional_validation.messenger.exception_unwrapper:
        class: PhPhD\ExceptionalValidationBundle\Adapter\Messenger\MessengerExceptionUnwrapper
        decorates: phd_exceptional_validation.exception_unwrapper.stack
        arguments:
            - '@.inner'
            - '@phd_exceptional_validation.exception_unwrapper'

```