**Identity Map** is an isolated subset of entities that correspond to some unique characteristic.

When entity defines a unique key, querying the [[ORM Collection|Collection]] by this key would not result in a database query. Instead, [[Query]] method will return the entity from the map.

It solves [[Identity map lookup limitations]].

One [[ORM Collection]] might have multiple identity maps - one per each unique [[Specification Criteria]].
