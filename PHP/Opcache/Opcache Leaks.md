The main [[Opcache]] problem that could arise is when it's being constantly reset:

![[Opcache restarts.png]]

You can find real calls to `opcache_reset` using [[phpspy]].
In their case, it was to use `opcache_invalidate($file)` instead.

