**Hierarchical Centroids** are aiming to constitute a hierarchical clustering or multi-level indexing.  
  
## The Idea  
  
[[Vectors Centroid|Centroids]] can be clustered into "super-[[Vectors Centroid|Centroids]]"
  Creates a tree structure
  Faster navigation at query time
  
```  
Level 2:        [Super-centroid A]     [Super-centroid B]  
                    /       \              /       \  
Level 1:       [C1]  [C2]  [C3]       [C4]  [C5]  [C6]  
                /|\   /|\   /|\        /|\   /|\   /|\  
Level 0:       vectors...             vectors...  
```  
  
## How Query Works  
  
```  
Query vector  
    ↓  
Find nearest super-centroid → A  
    ↓  
Find nearest centroid within A → C2  
    ↓  
Search vectors in C2  
```  
  
Each level reduces search space dramatically.  
  
## Real Implementations  
  
**FAISS IVF-Hierarchical:**  
  Multiple levels of quantization  
  `IndexIVF` can be nested  
  
**HNSW (graph-based):**  
  Similar principle  
  Higher layers = fewer nodes, bigger jumps  
  Lower layers = all nodes, fine search  
  
**SPANN (Microsoft):**  
  Hierarchical balanced clustering  
  Used in production at scale  
  
## Why It Helps  
  
Flat index with 1M vectors, 1000 centroids:  
  Compare query to 1000 centroids  
  Then search ~1000 vectors  
  
Two-level with 1M vectors:  
  Compare to 32 super-centroids  
  Compare to 32 sub-centroids  
  Search ~1000 vectors  
  
Reduced centroid comparisons: 1000 → 64  
  
## Trade-off  
  
More levels = faster search  
  But **less accurate** (more approximation)  
  And more complex index structure
