---
aliases:
  - Customer/Supplier
---
**Customer/Supplier** is **cooperative [[Context Integration Strategies|Relationship]]** in which one
(**upstream**) [[Bounded Context|Context]] *provides* **subset *of* the [[Domain Model|Model]]** to another
(**downstream**) [[Bounded Context|Context]]. Systems dependency is unidirectional.


![[Customer-Supplier.png]]

Key **problems** include:
- **upstream's freedom** is *hindered* by **downstream's [[Backward Compatibility|BC]]** requirement;
- **downstream** is *dependent* on **upstream's priorities**.

> **[[Customer-Supplier|Customer/Supplier]]** *is* ***not* poor-cousin** relationship. 
> **Customer's priorities** *are* **paramount**.

To solve a **[[Backward Compatibility|BC]] issue**:
- **Teams** should jointly *develop* the **interface acceptance tests** *and* set up to ***run* on the upstream's [[Continuous Integration|CI]]** 
	- It's vital in customer relationship, lest on change the upstream will fall short and *\[to prevent\]* **emergency fixes** will have to be developed, disrupting the normal work flow.

To solve the **priorities issue**:
- Do **cross-team** iteration **planning**:
	- **Supplier's planning** should be extended to
	   *take into account* **customer's concerns**:
		- **Supplier** will *get* the **priorities** *of* the **customer**, 
		- *and* the **customer** will *know* the **ETA**.
	- **Customer** team members should be 
	  *available* **during the iteration** just in case of 
	  any questions.

[[Customer-Supplier]] relationship works **well** *under* **the same management**:
- Two teams must have **shared interests**.
- The **upstream team** must be **motivated to serve**.

