---
aliases:
  - summary-features
---
Same as [[Match Features]], but computed only for the **final result hits** (trip from container to content node), not all matched candidates.

Cheaper, but unsuitable for LTR training data collection.

## Match vs Summary -Features

|              | `match-features`                   | `summary-features`               |
| ------------ | ---------------------------------- | -------------------------------- |
| Computed for | **All** matched hits (first-phase) | Only the **final** returned hits |
| Cost         | Higher (runs on every candidate)   | Lower (runs on top N)            |

