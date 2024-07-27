The [[Garbage collection]] may run in the least suitable moment. 
It is possible to mitigate this by doing GC as a planned short node outages:
- **periodically restart processes** - like with [[Rolling upgrade|rolling upgrade]] other nodes may be notified that current node won't handle traffic (or it would look like failed) and traffic distributes to other nodes;
- **inform applications about GC** starting soon so that they will not send traffic and when all running requests will finish, GC will run.