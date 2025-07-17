See: [[ORM]] [[Repository]] [[Reactive collection]]

ORM [[Repository]] represents a Collection of all the objects of a certain type.

## Features, good to have

It should support:
- index fields (e.g. access by O(1))


It should enable eager loading, preventing N+1 query problem.

`$users->map(fn($user) => $user.getPosts()->map(...))`

This should load posts for all the users that are currently being `map`-ped in one request.

Its lazy loading would be very well with column-oriented databases (for example, posts->map(p.getCategory())) will hydrate only `category_id` into object, not doing anything else to the posts themselves.
