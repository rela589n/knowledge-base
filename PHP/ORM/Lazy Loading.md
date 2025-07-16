Lazy Loading should use [[Column Loading]] approach.

When [[Criteria Collections|Collection]] is being loaded, each object should include no more than what [[Specification]] says (plus primary id). So, if filter was by `email`, then objects returned will have `id` and `email` fields only.
