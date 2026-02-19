---
aliases:
  - fieldsets
---
**Fieldset** - a query-time grouping of multiple fields
	under a single name
	for searching across them simultaneously.

---
### Why Use Fieldsets?

Problem: you want to search `title`, `body`, `summary` at once
	without writing: `title:query OR body:query OR summary:query`

Solution: define a fieldset
```vespa
fieldset content {
    fields: title, body, summary
}
```

Now query simply:
```
content:query
```

---

### Key Characteristics

**No extra storage**
  - purely a query-time mapping
  - no additional index structures created

**Default fieldset**
  - name it `default` to use when no field specified
  ```vespa
  fieldset default {
      fields: title, body
  }
  ```
  - query `?query=hello` searches both title and body

---

### Configuration Options
?is it?
```vespa
fieldset myfieldset {
    fields: a, b, c

    match {
        exact           # override match mode for all fields
    }
}
```

---

### Important Constraint

Fields in a fieldset should have **similar settings**:
  - same indexing type
  - same [[Match Mode]]

Mixing different match modes
  → deployment warning
  → unpredictable behavior

```vespa
# Bad: mixing index and attribute fields
fieldset mixed {
    fields: indexed_field, attribute_field # WARNING
}

# Good: similar fields
fieldset text_content {
    fields: title, description, summary # OK - all are indexed text
}
```

## See Also

- [[Schema]]
- [[Match Mode]]s
