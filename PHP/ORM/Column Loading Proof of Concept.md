```php
<?php

require "/app/vendor/autoload.php";

$entityLoader = new EntityLoader();

$user1 = new UserProxy($entityLoader, 1);
$user2 = new UserProxy($entityLoader, 2);

$posts = new Collection([
    new PostProxy($entityLoader, 1, $user1),
    new PostProxy($entityLoader, 2, $user2),
    new PostProxy($entityLoader, 3, $user2),
]);

// posts = this.getPosts();
// posts.map((p) => p.getUser().getManager()->getSm())

// N+1: 10 posts = up to 20 queries,
// but NO! It's only 2 queries
$managers = $posts
    ->map(fn (Post $post) => $post->getUser()->getManager());

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

        $this->entityLoader->load('user', $this);

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

        $this->entityLoader->load('manager', $this);

        return parent::getManager();
    }
}


class EntityLoader
{
    private array $pendingLoad = [];

    public function load(string $class, $item): void
    {
        $this->addPendingLoad($class, $item);

        \Amp\delay(0);

        $this->doLoad($class);
    }

    private function addPendingLoad(string $class, $item): void
    {
        $this->pendingLoad[$class][] = $item;
    }

    private function doLoad(string $class): void
    {
        if (empty($this->pendingLoad[$class])) {
            return;
        }

        var_dump('loading entities: ' . $class);
        var_dump($this->pendingLoad[$class]);

        $this->pendingLoad[$class] = [];
    }
}

class Collection
{
    public function __construct(
        private array $items,
    ) {
    }

    public function map(Closure $callback): self
    {
        $futures = [];

        foreach ($this->items as $item) {
            $futures[] = \Amp\async($callback, $item);
        }

        $results = \Amp\Future\await($futures);

        return new static($results);
    }
}
```