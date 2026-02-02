---
aliases:
  - Vespa Namespace
---
**Namespace** - a logical grouping that isolates documents of the same schema.

## Purpose

- Partition documents without duplicating [[Schema|Schemas]]
- [[Multi-Tenancy]]: one namespace per customer

### Example

Same `product` schema, different namespaces:
- `id:customerA:product::1`
- `id:customerB:product::1`

Query with `namespace=customerA` → only sees their data.

### Document ID Structure

```
id:mynamespace:book::123
   ─────┬───── ──┬── ─┬─
     namespace  schema  local ID
```
