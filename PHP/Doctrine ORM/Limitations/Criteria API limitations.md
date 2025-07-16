Criteria API is a great [[Specification]] thing, but it's with its own limitations. 

<u>It's not possible to filter by non-direct object field.</u> That what you'd usually do as leftJoin (with filter) in query builder isn't possible.

Besides that, currently [[Doctrine ORM]]  provides way to do `$repository->matching($criteria)`, and it returns `LazyCriteriaCollection`. 

Yet, it's not possible to chain `matching` calls, since it results in collection load:

```php
    /** @return ReadableCollection<TKey, TValue>&Selectable<TKey, TValue> */
    public function matching(Criteria $criteria): ReadableCollection&Selectable
    {
        $this->initialize();
        assert($this->collection instanceof Selectable);

        return $this->collection->matching($criteria);
    }
```

Note that `$this->initialize();` is called.

