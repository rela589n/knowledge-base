First of all, when you create `new Entity()`, it creates `new EntityProxy()` so that it can be tracked by ORM.

Then, when we add this new entity to the collection, there might be some relationships in place that are not connected to the ORM engine itself.

For example:

```php
public function __construct(Uuid $id)
{
    $this->id = $id;
    $this->posts = new PostCollection();
    $this->comments = new PostCommentCollection();
	// some posts could be added
}
```

These relationships aren't connected.

When kick-in happens, all such relationships must be analyzed and replaced with Auto-wired alternatives, and all the items present in these collections must be moved to the User's collections. 

Entries are moved from the fields of the stub entity into the fields of the real Ghost.
