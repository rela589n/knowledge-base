---
aliases:
  - Vespa Virtual Field
---
**Synthetic field** — a schema field defined *outside* `document {}`
that derives its value from document fields at index time.

## Document vs Synthetic

```
schema mySchema {
  document mySchema {
    field myField type string { ... } # document field
  }

  field mySyntheticField type tensor(x[386]) {   # synthetic field
    indexing: input myField | embed | attribute | index
  }
}
```

| Aspect         | Document field      | Synthetic field               |
| -------------- | ------------------- | ----------------------------- |
| Defined in     | `document {}` block | Outside `document {}` block   |
| Source         | Input data (PUT)    | Computed from document fields |
| Stored on disk | Yes                 | Yes                           |

## Use cases

**Auto-generate embeddings:**

```
field embedding type tensor(x[386]) {
    indexing: input myText | embed my-embedder | attribute | index
}
```

**Prefix search on terms:**

```
field title_tokens type array<string> {
    indexing: input title | trim | split " +" | attribute
    attribute: fast-search
}
```

- Regular `index` fields don't support prefix matching
- Splitting into array + `fast-search` enables prefix queries on individual terms

**LLM enrichment:**

```
field generated_questions type string {
    indexing: input text | generate my-llm | summary | index
}
```

- Generate questions or summaries at index time
- Useful for improving recall

**Chunking (v8.520+):**

```
field chunks type array<string> {
    indexing: input text | chunk sentence | attribute
}
```
