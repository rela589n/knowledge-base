---
aliases:
  - LLM
---
**Large Language Model** - a big bunch of weights (numbers).

Training the model - finding the right weights.

## LLM Text Processing

### Tokenization

Text's split into subword tokens and looked up for [[Token Embedding Matrix|Embedding Matrix]].

### Static vs Contextual Embeddings

Initial embeddings are just starting points
  - "bank" always starts as the same vector regardless of context

Transformer layers create contextual representations
  - Self-attention lets tokens "communicate"
  - Each layer refines representations based on surrounding tokens
  - After N layers: "bank" near "river" differs from "bank" near "money"

### Processing Flow

```
Text → Tokens → Static embeddings (lookup)
    → + Positional encoding
    → Transformer layers (context emerges)
    → Final contextual representations
    → Next token prediction
```
