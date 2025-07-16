When we persist new entity, there might be some relationships in place that are not connected to ORM engine itself.

For example:

```php
public function __construct(Uuid $id)
{
    $this->id = $id;
    $this->posts = new PostCollection();
    $this->comments = new PostCommentCollection();
}
```

These relationships aren't connected.

When kick-in happens, all such relationships must be analyzed and replaced with Auto-wired alternatives. This process should include all the entities that might have been added to this collections (these are moved to real `PostCollection` and `PostCommentCollection`).
