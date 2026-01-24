---
aliases:
  - HyDE
---
**HyDE** - [[Retrieval-Augmented Generation|RAG]] approach where you embed a *generated answer* instead of the raw query.

### Why it helps

- Queries are short and vague
- Documents are long and detailed
- A hypothetical answer is structurally closer to real documents
  - Better vector similarity match

### How it works

```
1. User query: "How does photosynthesis work?"
                ↓
2. LLM generates hypothetical answer:
   "Photosynthesis is the process by which plants
    convert sunlight into energy using chlorophyll..."
                ↓
3. Embed this hypothetical document
                ↓
4. Retrieve real documents similar to it
```

### Key insight

- The hypothetical answer doesn't need to be correct
- It just needs to *sound like* a relevant document
  - Uses similar vocabulary
  - Has similar structure
  - Lives in the same embedding space region

### Trade-off

- Extra LLM call adds latency and cost
- But retrieval quality often improves significantly
  - Especially for abstract or vague queries
