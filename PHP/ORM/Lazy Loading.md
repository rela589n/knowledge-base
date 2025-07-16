When [[Criteria Collections|Collection]] is being loaded, each object should include no more than what [[Specification]] says (plus primary id). So, if filter was by `email`, then objects returned will have `id` and `email` fields only.

On field is accessed, only then should it be loaded. The approach to load should be [[Column Loading]] approach.

For example, if we've selected user by `email=test@test.com`, and then access `password` property, only then should it be loaded from the database.
