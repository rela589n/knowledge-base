AKA, durable execution, - stateful function that guarantees execution of the code. Under the hood it automatically deals with problems like timed-out apis, database failures and so on.

You don't need to think about process crashes all the time.

It exposes configuration for exponential retries, rate limiting, flow control.