When [[Criteria Collections|Collection]] is being loaded, each object should include no more than what [[Specification]] says (plus primary id). So, if filter was by `email`, then objects returned will have `id` and `email` fields only.

On field is accessed, only then should it be loaded. The approach to load should be [[Column Loading]] approach.

For example, if we've selected user by `email=test@test.com`, and then attempt to access `password` property, only then should `password` column be loaded from the database.

#### Combinable Proxies

In case if we have a lazy proxy, mapped by secondary key (for example, Post is mapped by User email), then this proxy could possibly conflict with another proxy. 

I mean we have `User{email: foo}`, and we could have another `User{id: 2}`, and these two are same. Two users are the same, but how do we know it? If we do nothing when creating `User{email: foo}` proxy when there already was `User{id: 2}` in heap, at some point we must combine them into `User{id: 2, email: foo}`.

Two proxies must be adjusted to point to the same object.