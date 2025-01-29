Often domain has natural bias of association. 

The many-to-many may be reduced to unidirectional one-to-many if only one side needs the traversal ability.

It is good to keep associations unidirectional whenever possible.

> For example, `Country - President` relationship should usually be unidirectional `one-to-many`, since in the domain we aren't asked "what country Washington was the president of?" Conversely, we ask who was the president of the country at some moment of time. Thus, it's not necessary to bloat Person entity just for the sake of bidirectional relationship.
