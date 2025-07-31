In case if we have a [[Lazy Loading|Lazy]] Ghost Proxy, mapped by a secondary key (for example, `Post.owner` is mapped by `User.email` instead of `id`), then there's a possibility for this proxy to collide with another proxy (mapped by `id` for example). 

Let's say we have `User{email: foo}`, and another `User{id: 2}`, and yet these two Proxies are the same Entity. 

Two users are the same, but how and when do we know it? If we do nothing additional (like querying the database) when creating `User{email: foo}` proxy, `User{id: 2}` being already in the heap, we won't know that they are the same until either side of the classes gets more full information about [[Entity Identity]] (for example, unique column).

1. When Proxy is created, it must be checked if there's already one identified by at least one of the unique keys. In this case, the existing object can be used.
2. When Proxy is loaded, point of our interest is in unique keys that become complete. At this point, it must be checked if there's another Proxy with the same unique key. If so, both must be adjusted, and one of them will become Link Proxy.

For the second scenario, two proxies must be adjusted to the same conceptual object.

At some point we must combine `User{email: foo, ...}` and `User{id: 2, ...}` into `User{id: 2, email: foo}`, and maintain state for both of them. See [[Proxies Merge.canvas|Proxies Combination]]

We might create Link Proxy pointing to Ghost object using 
native means of PHP. When it's necessary to combine them, one ghost is merged into another, and it's reset as proxy toward the merged ghost. And it's discarded from identity heap. It's safe to discard it, because now it proxies access to the real Ghost.

Thus, if one Link Proxy object is updated, the Ghost is updated as well, since it's forwarded toward the same Ghost. If one object gets property loaded, the other does so as well. If one is updated, the other is updated as well.
