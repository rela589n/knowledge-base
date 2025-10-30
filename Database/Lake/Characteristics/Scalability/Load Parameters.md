Load is described by **load parameters**. For instance, [[Request per second|RPS]] to server, cache hit rates, ratio of reads/writes to database, etc.

> Fan-out - number of requests to other services necessary to serve incoming request.

In case of Twitter, where avarage post tweet rate is 4.6k/sec and read 300k/sec tweets in timeline, the main load parameter is _how much followers are per user_. For instance, some people have over 40 million followers which need to be posted every time celebrity post tweet.