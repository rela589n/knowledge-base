---
aliases:
  - Centroid
---
**[[Embedding Vector|Vectors]] Centroid** is a <u>center point</u> of a group of [[Embedding Vector|Vectors]].
  
```  
        •  •  
      •   ✕   •      ← ✕ is the centroid  
        •  •  
```  
  
It's the <u>"average" position</u> of all points in a cluster.

![[Triangle Centroid.png]]
  
## How It's Computed  
  
```  
Vectors in cluster:  
  [1, 2, 3]  
  [2, 3, 4]  
  [3, 4, 5]  
  
Centroid = average of each dimension:  
  [(1+2+3)/3, (2+3+4)/3, (3+4+5)/3]  
  = [2, 3, 4]  
```  
  
## Why Centroids Matter for ANN  
  
Instead of comparing query to every [[Embedding Vector|Vector]]:  
  Compare to centroids first (few hundred)  
  Then search only the nearest cluster(s)  

```  
Query: "What is AI?"  
    ↓  
Compare to 100 centroids  
    ↓  
Nearest centroid: #42  
    ↓  
Search only vectors in cluster #42 (thousands, not millions)  
```  
  
## K-Means Clustering  
  
Most common way to create centroids:  
  
1. Pick K random starting points  
2. Assign each vector to nearest centroid  
3. Recompute centroids as cluster averages  
4. Repeat until stable  
  
Result: K clusters, each with one centroid