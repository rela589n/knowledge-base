ORM should implement [[Repository|Repositories]] as simple [[ORM Collection]] classes. These will allow to use [[Specification API]].

See [[Criteria Collection Example]].

See [[PHP Asymmetric Property Hook]]

Lazy Autowire

```php
#[Autowire]
private PostCommentCollection $comments {
    set => $value->ofPost($this->id);
}
```

On proxy this should be Auto-wired only when accessed.
