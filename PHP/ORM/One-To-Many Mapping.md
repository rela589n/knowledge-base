One-To-Many Mapping is completely based on [[Autowire Feature]]. It allows to map the relationship appropriately from the global collection:

```php
#[Autowire]
private PostCommentCollection $comments {
    set => $value->ofPost($this->id);
}
```
