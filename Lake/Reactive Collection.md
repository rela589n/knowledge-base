---
aliases:
  - Derived collection
---
The main collection could keep the weak map of the derived collections so that to update them all when it changes.

```php
$derived = $collection->filter(/*...*/);

$collection->push(123);

// dervied also has 123, if it satisfies the filter
```

> Is it necessary to have `derive()` method? Can't `filter` itself return a new derived collection, managed by it's parent?

If every collection in orm would have been reactive, then pushing new post to global `PostCollection`, from which every other collections (like `user.posts`) are derived would automatically update the derived collections.

See https://github.com/ReactiveX/RxPHP

```php
final class Collection
{
    private WeakMap $derivedCollections;

    public function __construct(
        private array $items,
        private array $operations,
    ) {
        $this->filterCollections = new WeakMap();
    }

    public function filter(Closure $callback): self
    {
        $filter = (new \loophp\collection\Operation\Filter())()($callback);

        $collection = new self($this->items, [...$this->operations, $filter]);

        $this->filterCollections[$collection] = $filter;

        return $collection;
    }

    public function diff(array $values)
    {
        // [a,b,c], [a, b] => [c]

        $diff = (new \loophp\collection\Operation\Diff())()($values);

        $collection = new self($this->items, [...$this->operations, $diff]);

        $this->derivedCollections[$collection] = $diff;

        return $collection;
    }

    public function push(mixed $item)
    {
        $this->items[] = $item;

        foreach ($this->filterCollections as $filterCollection => $filterFunction) {
            if (iterator_count($filterFunction([$item]))) {
                $filterCollection->push($item);
            }
        }
    }
}
```