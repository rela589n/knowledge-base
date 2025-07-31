Both storage and retrieval is implemented with [[Spec Collections]].

```php
final readonly class RegisterUserCommand
{
    public function __construct(
        private string $id,
        private string $email,
        private string $password,
    ) {
    }

    public function process(CollectionManager $collectionManager): void
    {
        /** @var Collection<User> $collection */
        $collection = $collectionManager->getCollection(User::class);

        $user = new User($this->id, $this->email, password_hash($this->password));

        $collection->add($user);

        $collectionManager->sync();
    }
}
```

After user has been added to the Collection, it's considered managed. Then, on `sync()`, it's inserted into the database.

