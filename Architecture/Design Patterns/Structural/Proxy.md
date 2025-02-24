Pattern, that provides client with an substitute object for the original object.

Example:
- **lazy initialization** (commonly used in doctrine orm and symfony di container)
- **white list** (some feature can only be accessed by some users)
- **particular days submission policy** (e.g. form could be only submitted from 5 to 25, but not in other days)
- **caching proxy** (returns stored responses instead of making api/database request)

> There's a slight difference to [[Decorator]] that [[Proxy]] could interrupt the execution of the code w/o calling the decorated object.