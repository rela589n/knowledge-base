In case if we have a [[Lazy Loading|Lazy]] proxy, mapped by secondary key (for example, `Post.owner` is mapped by `User.email`), then this proxy could possibly collide with another proxy. 

For example, having `User{email: foo}`, we could have another `User{id: 2}`, and these two Proxies are same Entity. Two users are the same, but how do we know it? If we do nothing when creating `User{email: foo}` proxy when there already was `User{id: 2}` in heap, at some point we must combine them into `User{id: 2, email: foo}`.

Two proxies must be adjusted to point to the same object:
1. When Proxy is created, it must be checked if there's already one identified by unique combination of keys.
2. When Proxy is loaded (unique key becomes complete), it must be checked if there's another Proxy with the same unique key. If so, both must be adjusted.

[[Proxy per Field approach]]