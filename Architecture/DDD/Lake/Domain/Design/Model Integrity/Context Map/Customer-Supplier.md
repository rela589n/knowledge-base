---
aliases:
  - Customer/Supplier
---
**Customer/Supplier** is **cooperative [[Context Integration Strategies|Relationship]]** in which one (upstream) [[Bounded Context]] **provides subset of the [[Domain Model|Domain Model]] to another** (downstream) [[Bounded Context]]. Systems dependency is unidirectional.

[[Customer-Supplier|Customer/Supplier]] is not poor-cousin relationship. 
**Customer's priorities are paramount**.

![[Customer-Supplier.png]]

Key problems include:
- **upstream freedom is hindered by downstream [[Backward Compatibility|BC]] requirement**;
- **downstream is dependent on upstream's priorities**.

To solve a [[Backward Compatibility|BC]] issue, the **interface acceptance tests** should be **jointly developed** and set up to **run on upstream's [[Continuous Integration|CI]]** . It's vital in customer relationship, lest on change the upstream will fall short and emergency fixes will have to be developed, disrupting the normal work flow.

To solve the priorities issue, it's necessary to do **cross-team iteration planning**. *Supplier's* planning should be expanded to **take into account *customer's* concerns**. *Supplier* will get the priorities of the *customer*, and the *customer* will know when to **expect delivered features**. Customer team members should be available during iteration just in case of any questions.

[[Customer-Supplier]] relationship works well under **the same management**. Two teams must have **shared interests**. The **upstream team** must be **motivated to serve**.
