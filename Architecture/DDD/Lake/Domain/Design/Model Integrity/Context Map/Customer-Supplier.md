---
aliases:
  - Customer/Supplier
---
**Customer/Supplier** - one (upstream) [[Bounded Context]] **provides subset of the [[Domain Model|Domain Model]] to another** (downstream) [[Bounded Context]]. Systems dependency is unidirectional.

![[Customer-Supplier.png]]

The problems include:
- **upstream freedom is hindered by downstream [[Backward Compatibility|BC]] requirement**;
- **downstream is dependent on upstream's priorities**.

To solve a [[Backward Compatibility|BC]] issue, the **interface acceptance tests** should be developed and established to run on upstream's [[Continuous Integration|CI]] .

To solve the priorities issue, it's necessary to do **cross-team iteration planning**. Supplier's planning should be expanded to **take into account Customer's concerns**. Supplier will get the priorities of the Customer, and the Customer will know when to expect delivered features.
