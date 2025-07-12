**Shared Kernel** is highly **cooperative [[Model Context Strategies|Relationship]]** between two [[Bounded Context|Bounded Contexts]], in which some **parts of the [[Code]]** (some entities) and other **[[Bounded Context Aspects|Aspects]] are physically shared**.

Useful when it's too much overhead for full [[Model Unification|Unification of the Models]]. We **synchronize only the *subset* of [[Domain Model|Model]] citizens**.

We only **reduce duplication**, not eliminate it completely compared to how it would've been in case of one [[Bounded Context]].

The explicitly **shared stuff** should be **changed** only by **consulting the other team**. All [[Continuous Integration]] **Tests of both teams must pass** in this case.

If team's [[Continuous Integration]] rate is once a day, then [[Shared Kernel]] [[Continuous Integration|Integration]] could be once a week.

Often [[Shared Kernel]] is [[Core Domain]], some set of [[Generic Subdomain]].
