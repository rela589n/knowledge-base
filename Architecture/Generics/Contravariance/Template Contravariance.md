---
aliases:
  - Contravariant
  - Input-variance
---
**Contravariance** allows **more generic** type be *passed* ***into*** a **specific** one (a descending variance).

`@template-contravariant` allows to pass `Juicer<Fruit>` into a `Juicer<Orange>` (<b><u>counter-inheritance</u></b> direction).

> Use when type can accept <b><u>more generic input</u></b>.

Contravariance is <b><u>safe</u> in input</b>, but <b><u>unsafe</u> in output</b>.

> **Parameter types** must be contravariant (same/more generic)
> to the interface ([[Liskov substitution principle]])

![[Contravariance by Christopher Okhravi.png]]