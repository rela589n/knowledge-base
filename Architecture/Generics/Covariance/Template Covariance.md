---
aliases:
  - Covariant
  - Output-variance
---
**Covariance** allows a **more specific** type be *passed* ***into*** a **generic** one (ascending variance).

`@template-covariant` allows to pass `Collection<Orange>` into a `Collection<Fruit>`.

> Use when type must produce <b><u>more specific output</u></b>.

Covariance is <b><u>safe</u> in return</b>, but <b><u>unsafe</u> in parameter</b>.
Thus, it your collection would not have `add(T)` method.

> **Return types** are covariant (same/more specific)
> to the interface ([[Liskov substitution principle]])

As you have an [[Template Invariance|Invariant template]], you can still accept a generic collection as a [[Template Covariance|Covariant one]] to run some read-code (doesn't modify the collection), it's possible to have **[[Runtime Variance]]**.

> **Assignment** is covariant:
> `fn(Fruit $f) => $f->weight;` can accept `Orange`.
> `Fruit $f = new Orange();` is allowed.


![[Covariance by Christopher Okhravi.png]]