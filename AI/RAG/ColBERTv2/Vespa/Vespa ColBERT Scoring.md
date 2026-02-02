Read inside-out:
```sd
expression: sum(                                 ← Step 3: sum over querytoken
  reduce(                                        ← Step 2: max over token (doc tokens)
    sum(                                         ← Step 1: dot product (sum over dim)
      query(query_embedding)                     ← qᵢ vectors: (querytoken{}, dim[128])
      * unpack_bits(attribute(colbert_embedding)), ← dⱼ vectors: (token{}, dim[128])
      dim
    ),
  	max,
  	token
  ),
  querytoken
)
```
