---
aliases:
---
**Document Summary** - a configuration that exposes fields
	to be returned in query results.

### The Core Idea

When querying Vespa, you don't need all fields back.

Document summaries define **views** over documents:
```
Full document:     [title, body, author, date, metadata, embeddings...]
                              ↓
Summary "short":   [title, author]
Summary "full":    [title, body, author, date]
```

### Default Summary

`default` is auto-generated with:
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

![[Document Summary.png]]

#### Limiting what's available

Summary defines what's **available to return** — a prerequisite.
Not every field should be exposed to clients.

YQL `select` then picks from that set at query time (client response shaping only — not a performance optimization).

A field outside of `summary` simply **cannot** be returned, even if requested.

#### Faster responses

[[Indexing Attribute field|Attribute]]-only summaries = faster responses:
```vespa
document-summary fast-summary {
    summary title {}      # attribute
    summary price {}      # attribute
    # skip the body on disk
}
```

**Bandwidth**
- return only what the client needs
- skip large fields (embeddings, full text)

**Performance considerations**
- attribute fields → memory-only (fast)
- non-attribute fields → disk I/O (slow)


### `select` vs `summary=` — Two Different Layers

**`select field1, field2` in YQL** — client-side projection only
- Content nodes still fetch **all default summary fields** from document store → container
- Container strips unwanted fields → sends only selected fields to client
- Saves client bandwidth only — no disk or network optimization

**`presentation.summary=` parameter** — actual content node optimization
- Content nodes fetch **only the declared fields** from document store
- Less disk I/O + less internal network traffic
- Real performance gain, especially with large hit counts and large documents

```
Default summary (with YQL select):
  content node → [ALL fields] → container → [strip] → [selected fields] → client

Custom summary (with summary= param):
  content node → [declared fields only] → container → [declared fields only] → client
```

> `select title` looks like an optimization — it isn't.
> For large hit counts, always use dedicated summary classes.

**Best practice — use both:**
- `presentation.summary=fast` → tells content nodes what to fetch (perf)
- `select title, price` → shapes the API response (hygiene)

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

### See Also

- [[Schema]]
- [[Indexing Attribute field]]
