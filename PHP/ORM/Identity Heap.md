If entity defines a unique key, and we have entity in identity map, we don't want to run a database query again. We should return this entity.

Identity Heap should be implemented per [[Criteria Collections|Collection]] basis.
