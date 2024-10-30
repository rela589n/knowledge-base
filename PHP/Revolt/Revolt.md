
By default, if no other event loop extensions are set up, Revolt uses `StreamSelectDriver`, that is built on top of native PHP `stream_select` function.

Yet, to gain the best performance, [[libuv]] extension is considered to be the best option performance-wise.

