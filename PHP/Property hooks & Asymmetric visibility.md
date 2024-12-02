```php
class Person
{
    public string $fullName {
        get => $this->firstName.' '.$this->lastName;
    }

    public string $doubleName {
        get => $this->fullName.' '.$this->fullName;
    }

    private array $posts = [];

    public array $activePosts {
        get => array_filter($this->posts, static fn (Post $p) => $p->isActive);
    }


    public function __construct(
        private(set) string $firstName,
        private(set) string $lastName,
    ) {
    }

    public function addPost(Post $p): void
    {
        $this->posts[] = $p;
    }
}

$p = new Person('John', 'Doe');

var_dump($p->firstName, $p->lastName, $p->fullName, $p->doubleName);
```