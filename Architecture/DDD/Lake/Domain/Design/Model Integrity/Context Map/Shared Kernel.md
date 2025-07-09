**Shared Kernel [[Relationships Between Bounded Contexts|Relationship]]** - two [[Bounded Context|Bounded Contexts]] physically share some parts of the [[Code]], holding shared entities.

Useful when it's too much overhead to fully sync the [[Domain Model|Models]].
We **synchronize only the *subset* of [[Domain Model|Model]] citizens**.
We don't remove the whole duplication, we just reduce it.

The explicitly **shared stuff** shouldn't be **changed** without **consulting the other team**.

All [[Continuous Integration]] **Tests of both teams must pass** when changes are made.

If team's [[Continuous Integration]] rate is once a day, then [[Shared Kernel]] [[Continuous Integration|Integration]] could be once a week.

Often [[Shared Kernel]] is [[Core Domain]], some set of [[Generic Subdomain]].
