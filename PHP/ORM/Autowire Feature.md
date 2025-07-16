`#[Autowire]` attribute allows to define properties that are automatically injected:

```php
#[Autowire]
private PostCommentCollection $comments {
    set => $value->ofPost($this->id);
}
```

> It allows to overcome [[Doctrine Custom Collections]] limitation, and gives a lot of customization.

It is lazily evaluated, meaning that `$comments` property will not be initialized until you first access it.

`#[Autowire]` can also be used to lazy-eagerly initialize property w/o need for doing this on getter:

```php
#[Autowire]
private PostCommentCollection $topComments {
    set => $this->comments->orderByRating()->limit(10);
}
```
