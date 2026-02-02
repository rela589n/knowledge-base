---
aliases:
  - Schema
---
**Schema** - describes data stored and computations over it (ranking).

> It's like a database table definition + query configuration + ranking logic.
> All in one file.

- Document fields = what you store
- Derived fields = what Vespa computes (embeddings, lengths)  
- Rank profiles = the brain of your search (scoring logic)  
- Fieldsets = convenience for multi-field search  
- Summaries = optimize response size (return only what's needed)

```sd
schema <name> {
  document <name> {
	  field <name> type <type> {
		  indexing: <pipeline>
	  }
  }

  rank-profile <name> {
	  first-phase {
		  expression: <scoring>
	  }
  }
}
```

See [[Indexing Pipelines]]

See also: [[Vespa Schema Changes]]