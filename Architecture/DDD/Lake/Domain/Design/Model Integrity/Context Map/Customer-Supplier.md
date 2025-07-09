---
aliases:
  - Customer/Supplier
---
**Customer/Supplier** - one (upstream) [[Bounded Context]] **provides subset of the [[Domain Model|Domain Model]] to another** (downstream) [[Bounded Context]]. Systems dependency is unidirectional.

![[Customer-Supplier.png]]

The problems include:
- **upstream freedom is hindered by downstream [[Backward Compatibility|BC]] requirement**;
- **downstream is dependent on upstream's priorities**.

To solve the priorities issue, it's necessary to make cross-team iteration planning. Supplier will know the priorities of Customer, and Customer will know when to expect features to be delivered.


