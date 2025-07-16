`#[Autowire]` attribute allows to define properties that are automatically injected:

```php
#[Autowire]
protected PostCommentCollection $comments {
    set => $value->ofPost($this->id);
}
```

> It allows to overcome [[Doctrine Custom Collections]] limitation, and gives a lot of customization.

It is lazily evaluated, meaning that `$comments` property will not be initialized until you first access it.

`#[Autowire]` can also be used to lazy-eagerly initialize property w/o need for doing this on getter:

```php
#[Autowire]
protected PostCommentCollection $topComments {
    set => $this->comments->orderByRating()->limit(10);
}
```

Technically it's possible to implement it lazily by [[PHP Property Hooks and Inheritance]].

```php
class Proxy extends Post
{
    protected PostCommentCollection $topComments {
        get {
            (fn() => $this->topComments = $this->container->get(PostCommentCollection::class))();

            return $this->topComments;
        }
    }
}
```