**One-To-Many** is implemented with scoped [[Spec Collection]].

For example, `post.comments` relationship:

```php
#[Autowire]
private PostCommentCollection $comments {
    set => $value->ofPost($this->id);
}
```

It uses two features:
- [[PHP Asymmetric Property Hook]]
- Lazy [[Autowire Feature]]

Basically, you can define any conceivable relationship you want, using your custom [[Spec Collection]] class.

Additionally, for a simple use case, you can use native collection:

```php
#[Autowire]
/** @var Collection<array-key,Comment> */
private Collection $comments {
    set => $value->where(new Equals('post.id', $this->id));
}
```

It doesn't express the code so good as the previous example, but for small entities, it might be easier.

On proxy this could be Auto-wired only when accessed.
