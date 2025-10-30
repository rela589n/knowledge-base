> **Atomic** - something that can't be broken down into parts.

**Atomicity** - the ability to **abort the [[Transaction]]** partway if any error occurs.

> **Example:** Questionnaire [[Aggregate]] can only be created as unit.

This allows us to easily roll back multiple statements bound with [[Temporal Coupling|temporal coupling]] in one operation.