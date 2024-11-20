Service represents an operation offered to the client. It doesn't have the state on it's own. 

It should accept parameters as domain objects and return results as the domain objects as well.

Could the domain service be replaced with the domain event? Like `MoneyTransferredEvent.process()` that uses two accounts to debit and credit the money.

> Services MUST not strip the entities of their behavior.

> Technical Services (like sending the email) should lack any domain meaning at all.
