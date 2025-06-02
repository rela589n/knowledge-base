See `\Temporal\Api\Failure\V1\ApplicationFailureInfo::$next_retry_delay`

`next_retry_delay` can be used by the client to override the activity retry interval calculated by the retry policy. Retry attempts will  still be subject to the maximum retries limit and total time limit defined by the policy.
