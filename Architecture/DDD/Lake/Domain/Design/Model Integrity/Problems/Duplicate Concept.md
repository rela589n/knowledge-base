---
aliases:
  - Concepts are Duplicated
---
**Duplicate [[Domain Concept|Concept]]** is when there are two **distinct things** (and thus implementations) are the **same [[Domain Concept|Concept]]**.

The main **problem** is *maintaining* them **synchronized**:
- Every time **one** *is* **changed**, the **other** *must* **also**.

> **For example**, 
> If the [[Specification]] broken down, it would result in [[Duplicate Concept]] (one for db, one for object check).

Special case of duplicate is [[Dialect Concept]].
