ORM should implement [[Repository|Repositories]] as simple [[ORM Collection]] classes. These will allow to use [[Specification]] to work both over normal objects, and over database.

For example:

```php
/** @var PostCommentCollection $posts */
$posts = new PostCommentCollection(...);
$posts
    ->ofAuthor($authorId)
    ->ofPost($postId)
    ->orderByRating()
    ->limit(10)
    ->toArray();
```

This is much better than doing one method per use case, making it non-reusable for other use-cases.

```php
#[Autoconfigure(constructor: 'create')]
final readonly class PostCommentCollection
{
    public function __construct(
        /** @var Selectable<PostComment>&Collection<PostComment> */
        private Collection $collection = new ArrayCollection(),
    ) {
    }

    public function ofPost(Uuid $postId): self
    {
        /** @var ExpressionBuilder $expr */
        $expr = Criteria::expr();

        $criteria = Criteria::create()->where($expr->eq('post', $postId));

        return new self($this->collection->matching($criteria));
    }

    public function ofAuthor(Uuid $userId): self
    {
        /** @var ExpressionBuilder $expr */
        $expr = Criteria::expr();

        $criteria = Criteria::create()->where($expr->eq('author', $userId));

        return new self($this->collection->matching($criteria));
    }

    public function add(PostComment $comment): void
    {
        $this->collection->add($comment);
    }

    public function orderByRating(): self
    {
        $orderCriteria = Criteria::create()->orderBy(['rating' => Order::Descending]);

        return new self($this->collection->matching($orderCriteria));
    }

    public function contains(PostComment $comment): bool
    {
        // get method should just load only this one comment (proxy by id)
        return $this->collection->containsKey($comment->getId()->toString());
    }

    public function limit(int $limit): self
    {
        $maxResultsCriteria = Criteria::create()->setMaxResults($limit);

        return new self($this->collection->matching($maxResultsCriteria));
    }

    public function get(Uuid $id): PostComment
    {
        return $this->collection->get($id->toString()) ?? throw new EntityNotFoundException($id);
    }
}
```
