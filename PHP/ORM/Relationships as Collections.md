See [[PHP Asymmetric Property Hook]]

Lazy [[Autowire Feature]]

```php
#[Autowire]
private PostCommentCollection $comments {
    set => $value->ofPost($this->id);
}
```

On proxy this should be Auto-wired only when accessed.

Thus, you can define any conceivable relationship you might want with any conditions you would like, joining as many entities as necessary.
