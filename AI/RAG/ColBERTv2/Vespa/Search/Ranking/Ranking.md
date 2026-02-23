---
aliases:
  - Rank Profiles
  - rank-profile
---
**Rank Profile** - defines how to score and order matching documents.

- Default uses [[nativeRank()]]
- Selected via `ranking.profile` query parameter
- `unranked` skips scoring for performance

## Ranking Phases

Vespa ranks in layers, progressively refining results:

1. **First-phase** — all matching documents - when request's scattered to the **content nodes**
	- Fast, lightweight expressions
2. **Second-phase** — top k docs (1000/node)
	- More expensive models
3. **Global-phase** — after merging across nodes
	- Final reranking (typically top ~20)

## Rank Features

| Category | Purpose          | Example                 |
| -------- | ---------------- | ----------------------- |
| Document | Field values     | `attribute(popularity)` |
| Query    | Input from query | `query(userWeight)`     |
| Match    | Built-in signals | `bm25(text)`, proximity |

## Example

```sd
rank-profile semantic inherits default {
    inputs {
        query(q) tensor<float>(x[384])
    }
    first-phase {
        expression: closeness(field, embedding)
    }
    second-phase {
        expression: 0.7 * closeness(field, embedding) + 0.3 * attribute(popularity)
    }
}
```

## ML Model Integration

Supports inference of pre-trained models as rank features:
- ONNX (TensorFlow, PyTorch, scikit-learn)
- XGBoost
- LightGBM

See also: [[Schema]]
