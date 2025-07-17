In case if we have a [[Lazy Loading|Lazy]] proxy, mapped by secondary key (for example, `Post.owner` is mapped by `User.email`), then this proxy could possibly collide with another proxy. 

For example, having `User{email: foo}`, we could have another `User{id: 2}`, and these two Proxies are same Entity. 

Two users are the same, but how do we know it? If we do nothing when creating `User{email: foo}` proxy when `User{id: 2}` is already in the heap, we won't know that they are the same until either side of the classes gets information about one more unique column. 

1. When Proxy is created, it must be checked if there's already one identified by some of the unique keys. In this case, existing object can be used.
2. When Proxy is loaded (unique key becomes complete), it must be checked if there's another Proxy with the same unique key. If so, both must be adjusted.

For the second scenario, two proxies must be adjusted to point to the same object.

At some point we must combine `User{email: foo, ...}` and `User{id: 2, ...}` into `User{id: 2, email: foo}`, and maintain state for both of them. See [[Proxies Merge.canvas|Proxies Combination]]

Consider that we create lazyProxy toward ghost object using 
native means of PHP. When it's necessary to combine them, ghosts are merged, and one proxy is reset to point toward the merged ghost. Another ghost is discarded. It's safe to discard it, since it's never referenced outside of the scope of the proxy. E.g. `$proxy === $proxy->getThis()` is always kept.

Thus, if one proxy object is updated, the second is updated as well since they point to the same ghost. If one object gets property loaded, the other does so as well. If one is updated, the other is updated as well.
