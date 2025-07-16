ORM should implement [[Repository|Repositories]] as simple [[ORM Collection]] classes. These will allow to use [[Specification]] to work both over normal objects, and over database.

See [[Criteria Collection Example]].

When Collection is being loaded, each object should include no more than [[Specification]] says (and probably primary id). So, if filter was by `email`, then objects returned will have `id` and `email` fields hydrated.

