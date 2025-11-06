**Identity Set** is a subset of the [[ORM Collection|Collection]] based on some [[Specification Criteria]].

It allows to prevent round trips for already issued queries.

For example, `$commentCollection->ofPost($post->id)` represents a <u>full set</u> of comments by this post. 

Running the same query method won't result in a round-trip.
