---
aliases:
  - Key-Range Partitioning
  - Partitioning by Key Range
---
Each [[Partition]] holds values for a **range of keys**. 

We can definitely **know which [[Partition]] holds which key** since we know the ranges of each [[Partition]].

## Partition Boundaries

Partition **boundaries** need to **adapt to the data**, not to the amount of possible keys. For example, in the dictionary there are a lot less words starting from X and Z than from A and B. 

**Boundaries** may be **chosen manually** by admin or **automatically**.
The **keys** inside [[Partition]] **are sorted** in order to make **easy range scans**.

## Partitioning By multiple fields (keys)

It is allowed to **[[Partitioning|Partition]] data by multiple keys**. It's important to select the **first element of the key** such field that will allow to **spread write load** across the [[Partition|Partitions]].

For instance, when sensor name and timestamp are used as keys, one single [[Partition]] would correspond to one type of sensors for one specific day (keys inside may hold different sensor names and different timestamps).
