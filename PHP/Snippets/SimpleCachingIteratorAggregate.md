
```php
public function getIterator(): Generator
{
    $cachedItems = &$this->iterator->getCache();

    $iterationMap = array_fill_keys(array_keys($cachedItems), true);

    yield from $cachedItems;

    while ($this->iterator->hasNext()) {
        $this->iterator->next();

        $iterationMap[$this->iterator->key()] = true;

        yield $this->iterator->key() => $this->iterator->current();

        if (count($cachedItems) === count($iterationMap)) {
            // no extra item was added to the cache since last yield iteration

            continue;
        }

        $extraCache = array_diff_key($cachedItems, $iterationMap);

        $iterationMap += array_fill_keys(array_keys($extraCache), true);

        yield from $extraCache;
    }
}
```