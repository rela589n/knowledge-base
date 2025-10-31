**Read-Modify-Write** - **Plain assignment** / **Rewrite**. 
Fraught with [[Lost Update]].

**It *does* "overwrite"** regardless:
- counter increment ;
- balance changes;
- local change in a complex value (say adding json field);
- full update of the object (say, two users modify some entity in admin panel).
