Implementation of [[Architecture/Design Patterns/Unit of Work|Unit of Work]] pattern.

Any operations that could run async will run async.

It means that operations graph is traversed and those queries that could run in parallel would be prepared in parallel.

Eventually, you can only run one SQL statement over one connection at a time, so we'll have to wait, but nonetheless, it could be changed in the future.
