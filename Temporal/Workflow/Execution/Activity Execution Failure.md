When you pass **bad parameters** (incompatible by types), the [[Activity]] is [[Retry Policy|Retried]].

If [[Schedule-To-Close]] timeout is specified it will be retried until this timeout is reached. Otherwise, if [[Retry Policy]] is specified, it will fail until it reaches max number of attempts. If neither is specified, it will be retried indefinitely. ^8c045a

If you want to avoid retrying (raise [[Permanent Failure]]), you can throw `ApplicationFailure` with `nonRetryable: true`.
