`#[Autowire]` attribute allows to define properties that are automatically injected:

```php
#[Autowire]
private PostCommentCollection $comments {
    set => $value->ofPost($this->id);
}
```

It is lazily evaluated, meaning that `$comments` property will not be initialized until you first access it.
