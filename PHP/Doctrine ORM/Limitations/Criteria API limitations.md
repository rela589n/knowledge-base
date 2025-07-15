Right now [[Doctrine ORM]]  provides way to do `$repository->matching($criteria)`, and it returns `LazyCriteriaCollection`. 

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

