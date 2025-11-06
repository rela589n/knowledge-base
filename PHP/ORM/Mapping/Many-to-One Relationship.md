
### Mapping id Column

Say we have `Comment` class:
```php
#[Column(name: 'post_id')]
private Uuid $postId;
```

Actually, the only necessary information for ORM is the column name. It doesn't even need [[Foreign Key]] information to make relationship to work. Yet, for relationship fields, one could define it to make migrations work correctly:

```diff
 #[Column(name: 'post_id')]
+#[ForeignKey(table: 'posts', column: 'id', onDelete: RefAction::CASCADE, onUpdate: RefAction::CASCADE)]
 private Uuid $postId;
```

When we delete `Post` entity, all its comments will be deleted as well.

