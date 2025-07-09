---
aliases:
  - Customer/Supplier
---
**Customer/Supplier** - one (upstream) [[Bounded Context]] **provides subset of the [[Domain Model|Domain Model]] to another** (downstream) [[Bounded Context]]. Systems dependency is unidirectional.

![[Customer-Supplier.png]]

The problems include:
- **upstream freedom is hindered by downstream [[Backward Compatibility|BC]] requirement**;
- **downstream is dependent on upstream's priorities**.

To solve the priorities issue, it's necessary to make **cross-team iteration planning**. Customer joins Supplier's planning, and he'll know the priorities of the Customer, and the Customer will know when to expect the features to be delivered.
