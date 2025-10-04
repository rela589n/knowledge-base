Initial **situation**: 
  you have a bunch of **new systems**
	  *that* **communicate** *with* **[[Legacy]]** 
		  *through* **[[Anti-Corruption Layer]]**.

You should ***cover* new systems** with **[[Testing|Tests]]**.

**Phase out** features in **small**, **iteration**-sized units. 
Don't get all features in one go.

1. Select a small set of **features** for the **iteration**;
2. **Identify** additions for **[[Anti-Corruption Layer]]**;
3. **Implement** feature;
4. Deploy;

**Deployment** should also be as **iteration**-sized as features.

Then, in the **process of time**:
1. Delete unused [[Anti-Corruption Layer]];
2. Delete phased out features off the [[Legacy]] system.
