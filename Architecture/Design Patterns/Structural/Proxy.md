**Proxy** is a pattern that **provides** client with an **substitute** object **for the original** object.

Example:
- **lazy initialization**
	- doctrine lazy entities
	- symfony lazy services
- **white list**
	- some feature can only be accessed by **some users**
- **caching proxy**
	- returns stored responses instead 
	  of making api/database request
- **particular days submission policy**
	- form could be only submitted from 5 to 25, 
	  but **not in other** days

> There's a slight difference to [[Decorator]] that
> -> **[[Proxy]] could interrupt** the execution of the code **w/o calling** the decorated object.
