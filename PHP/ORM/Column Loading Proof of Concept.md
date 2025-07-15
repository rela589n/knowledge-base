```php
<?php

require "/app/vendor/autoload.php";

$entityLoader = new EntityLoader();

$user1 = new UserProxy($entityLoader, 1);
$user2 = new UserProxy($entityLoader,2);

$posts = new Collection([
    new PostProxy($entityLoader, 1, $user1),
    new PostProxy($entityLoader, 2, $user2),
    new PostProxy($entityLoader, 3, $user2),
]);

// posts = this.getPosts();
// posts.map((p) => p.getUser().getManager()->getSm())

// N+1: 10 posts = up to 20 queries,
// but NO! It's only 2 queries
$managers = $posts->map(fn (Post $post) => $post->getUser()->getManager());

// Firstly, Users are loaded at once 
// Then, Mangers are loaded at once

var_dump($managers);

class Post
{
    public function __construct(
        private int $id,
        private User $user,
    ) {
    }

    public function getUser(): User
    {
        return $this->user;
    }
}

class PostProxy extends Post
{
    public function __construct(
        private EntityLoader $entityLoader,
        int $id,
        User $user,
    ) {
        parent::__construct($id, $user);
    }

    public function getUser(): User
    {
        // if ($this->user is loaded) {
        //    return parent::getUser();
        // }

        $this->entityLoader->addPendingLoad([$this, 'user']);

        \Amp\delay(0);

        $this->entityLoader->load();

        return parent::getUser();
    }
}

class User
{
    public function __construct(
        private int $id,
    ) {
    }

    public function getManager(): int
    {
        return $this->id ** 2;
    }
}

class UserProxy extends User
{
    public function __construct(
        private EntityLoader $entityLoader,
        int $id,
    ) {
        parent::__construct($id);
    }

    public function getManager(): int
    {
        // if ($this->manager is loaded) {
        //    return parent::getManager();
        // }

        $this->entityLoader->addPendingLoad([$this, 'manager']);

        \Amp\delay(0);

        $this->entityLoader->load();

        return parent::getManager();
    }
}


class EntityLoader
{
    private array $pendingLoad = [];

    public function addPendingLoad($item): void
    {
        $this->pendingLoad[] = $item;
    }

    public function load(): void
    {
        if ([] === $this->pendingLoad) {
            return;
        }

        var_dump('loading entities');
        var_dump($this->pendingLoad);

        $this->pendingLoad = [];
    }
}

class Collection
{
    public function __construct(
        private array $items,
    ) {
    }

    public function map(Closure $callback)
    {
        $futures = [];

        foreach ($this->items as $item) {
            $futures[] = \Amp\async($callback, $item);
        }

        return new static(\Amp\Future\await($futures));
    }
}
```