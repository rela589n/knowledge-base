**Failure that** happened in the past **is likely to repeat** in the future.

An example is the failure due to a service **[[Rate Limiting|Rate Limit]]** being reached (next **requests won't succeed** until the limiter is reset).

**[[Retry Policy|Retries]] will help**, but they have to have more prolonged [[Exponential backoff|Backoff Coefficient]] compared to [[Transient Failure]] to avoid triggering the limit.
