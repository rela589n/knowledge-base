When you pass bad parameters (incompatible by types), activity is [[Retry Policy|retried]].

If [[Schedule-To-Close]] timeout is specified it will be retried until timeout is elapsed. Otherwise, if [[Retry Policy]] is specified, it will fail until it reaches max number of attempts. Otherwise it will be retried indefinitely. ^8c045a

If you want to avoid retrying (raise [[Permanent Failure]]), you can throw `ApplicationFailure` with `nonRetryable: true`.
