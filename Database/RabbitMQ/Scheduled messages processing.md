> There's native support for it: https://www.rabbitmq.com/blog/2015/04/16/scheduling-messages-with-rabbitmq

It is possible to implement "scheduled" for particular time message by means of so-called `DelayStamp` that uses [[Dead-letter exchange (DLX)]] under the hood.

The idea is very simple:
1. Have the queue that has no consumers - it will be used to buffer scheduled messages;
2. Specify dead-letter exchange to this queue
3. Publish the messages with `ttl` option.

Using time-to-live on the message, we could basically calculate what's the needed delay for the message to be processed on the particular time. 

For example, if right now is 18:08, and we want the message to be delivered at 18:10, we'd specify ttl as 2 minutes (actually `120_000` ms, as it is only accepted in ms).

