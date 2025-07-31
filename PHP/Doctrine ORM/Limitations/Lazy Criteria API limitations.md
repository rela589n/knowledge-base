Criteria API is a great [[Specification]] thing, but it's with its own limitations. 

(1) <u>It's not possible to filter by non-direct object field.</u> That what you'd usually do as leftJoin (with filter) in query builder isn't possible.

(2) IndexBy doesn't really work with matching() method 
https://github.com/doctrine/orm/issues/4693

(3) Besides that, [[Doctrine ORM]] currently provides a way to do `$repository->matching($criteria)`, and it returns `LazyCriteriaCollection`, yet that doesn't support further `matching` api.

It's not possible to chain `matching` calls, since it results in collection load:

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

