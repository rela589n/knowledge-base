This is an example of an asymmetric property hook:

```php
class Post
{
    public array $comments {
        get => array_filter($this->comments, static fn ($c) => $c & 1);
    }
}

$post = new Post();
$post->comments = [1, 2, 3, 4, 5, 6, 7, 8];
var_dump($post->comments); // 1, 3, 5, 7
```
