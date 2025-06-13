Each partition holds values for a **range of keys**. 

We can definitely **know which partition holds which key** since we know the range of each partition.

## Partition Boundaries

Partition **boundaries** need to **adapt to the data**, not to the amount of possible keys. For example, in the dictionary there are a lot less words starting from X and Z than from A and B. 

**Boundaries** may be **chosen manually** by admin or **automatically**.
The **keys** inside partition **are sorted** in order to make **easy range scans**.

## Partitioning By multiple keys (fields)

It is allowed to **partition data by multiple keys**. It's important to select the **first element of the key** such field, which will allow to **spread write load** across partitions.

For instance, when sensor name and timestamp are used as keys, one single partition would correspond to one type of sensors for one specific day (keys inside may hold different sensor names and different timestamps).
