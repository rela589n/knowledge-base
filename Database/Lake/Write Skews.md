---
aliases:
  - Phantoms
---
> Example: there should always be at least one doctor for every slot. Two doctors request sick leave at the same time for the same slot. Query checks that there are two doctors for this slot and both go off. As a result, no doctor is left. 
> See [[Examples of write skew|More examples of write skew]].

**Write skew** - generalization of [[Lost Updates|lost update problem]] (lost update happens to the same record, while write skew is about separate records). This is the anomaly when two **parallel transactions run read queries**, whereupon depends further **update logic**, which results in **logic executed in both cases** instead of one.

**Write skew** can happen **if write depends on presence/absence of some records**, while this **write may insert new or modify this set of records** on it's own. Hence, if two transactions read the value, first makes the modification, then second is not aware that subset has changed and write skew happens.

## Phantoms causing write skew

**Phantom** - the effect when the **write in one transaction changes the query result in another** after the time this query was executed. 

Basically phantoms are revealed when we read the set of records from the database twice. When we see a different set from the one we've seen it before, - that's a phantom.

The [[Write Skews|write skew]] pattern is following:
1. select **query** searches for rows that **match some condition**;
2. depending on the result of query, **app decides what to do** (either report an error or make the write);
3. if condition from step 2 is satisfied, app **makes a write and commits** the transaction. The committed **write affects the result of the query** from step 1.

## Solutions

See [[Solutions to write skew]].