One activity can run for 3 attempts from one context, and only for a single attempt from another context, since this is configured in the calling place.

The same is possible with messenger, but there you need to configure one more queue, and configure retry strategy there, and run a consumer for that queue.
