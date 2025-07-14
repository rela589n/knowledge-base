[[Doctrine Limitations]]

Right now it's only possible to lookup entity by id. If you find it by anything else, it will definitely run a database query, even though it might not be necessary.
