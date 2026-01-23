How close must these [[Embedding Vector|Vectors]] be to be considered close?

Short answer: **No fixed threshold. It's relative.**

### The training objective

- Similar pairs → pushed closer  
- Dissimilar pairs → pushed farther apart

It’s not “must be within X distance.”  
It’s “must be **closer than** dissimilar pairs.”

### Contrastive learning (simplified)

Batch example:

- `"refund"` ↔ `"money back"` (similar)  
- `"refund"` ↔ `"sunny weather"` (dissimilar)

**Goal:**

distance(`"refund"`, `"money back"`) < distance(`"refund"`, `"sunny weather"`)

The model kept adjusting weights until that inequality held.

### Loss function logic

- If the similar pair ended up farther than the dissimilar pair → high error → weights updated
- If the similar pair ended up closer than the dissimilar pair → low error → all good

### What “close” actually meant

“Close” = **closer to similar things** than to dissimilar things.

 "refund", "money back" - these two are closer to each other 
		 than to "sunny weather"

