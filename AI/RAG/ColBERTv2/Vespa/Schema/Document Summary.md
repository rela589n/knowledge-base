---
aliases:
---
**Document Summary** - a configuration that exposes fields
	to be returned in query results.

### The Core Idea

When you query Vespa, you don't always need all fields back.

Document summaries let you define **views** over your documents:
```
Full document:     [title, body, author, date, metadata, embeddings...]
                              ↓
Summary "short":   [title, author]
Summary "full":    [title, body, author, date]
```

---

### Default Summary

Vespa auto-generates a `default` summary containing:
- all fields with `summary` in their indexing statement
- system fields (`documentid`, `sddocname`)

```vespa
field title type string {
    indexing: index | summary    # included in default summary
}

field embeddings type tensor {
    indexing: attribute          # NOT in default summary
}
```

---

### Custom Summary Classes

Define in schema:
```vespa
document-summary short {
    summary title {}
    summary author {}
}

document-summary full {
    summary title {}
    summary body {}
    summary author {}
    summary date {}
}
```

Request in query:
```
/search/?query=hello&presentation.summary=short
```

---

### Why have `summary` in the first place?

Not every field should be exposed to clients.

`summary` in the schema defines what's **available** to return — a prerequisite.
YQL `select` then picks from that set at query time.

A field without `summary` simply **cannot** be returned in query responses, even if requested.

---

### Why Use Custom Summaries?

Creating attribute-only summaries = faster responses:
```vespa
document-summary fast-summary {
    summary title {}      # attribute
    summary price {}      # attribute
    # skip: body (on disk)
}
```

**Bandwidth**
- return only what the client needs
- skip large fields (embeddings, full text)

**Performance considerations**
- attribute fields → memory-only (fast)
- non-attribute fields → disk I/O (slow)

---

### Additional Features

**Field renaming** — expose field under different name:
```vespa
document-summary api {
    summary productName {
        source: title
    }
}
```

**Dynamic snippets** — highlight query terms in context:
```vespa
document-summary search-results {
    summary body {
        dynamic
    }
}
```
Returns: "...the **query term** appeared in this context..."

## See Also

- [[Schema]]
- [[Indexing Attribute field]]
