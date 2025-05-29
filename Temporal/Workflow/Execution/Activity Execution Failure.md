When you pass bad parameters (incompatible by types), activity is [[Retry Policy|retried]]. If it reaches max number of attempts, it's considered failed.

If you want to avoid retrying (for [[Permanent Failure]]), you can throw `ApplicationFailure` with `nonRetryable: true`.


