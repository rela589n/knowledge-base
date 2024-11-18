Service represents an operation offered to the client. It doesn't have the state on it's own. 

It should accept parameters as domain objects and return results as the domain objects as well.

Could the domain service be replaced with the domain event? Like `UserRegisteredEvent.process()` that "does" register the user.


> Services MUST not strip the entities of their behavior.

> Technical [[Service]] should lack any domain meaning at all.
