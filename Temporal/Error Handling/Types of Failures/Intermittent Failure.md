Failure that happened in the past is likely to repeat in the future.

An example is the failure due to a service [[Rate Limiting|rate limit]] being reached (requests won't succeed until limiter is reset).

Retries will help, but they have to have more prolonged [[Exponential backoff|backoff coefficient]] compared to [[Transient Failure]] to avoid triggering the limit.

