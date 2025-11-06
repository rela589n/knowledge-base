[[Doctrine Limitations]]

Right now it's only possible to lookup entity by id.
If you seek by anything else, it will run a database query, even though it might not be necessary.
