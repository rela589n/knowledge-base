One-To-Many Mapping is completely based on [[Autowire Feature]]. It both allows to overcome [[Doctrine Custom Collections]] limitation, and map the relationship appropriately:

```php
#[Autowire]
private PostCommentCollection $comments {
    set => $value->ofPost($this->id);
}
```
