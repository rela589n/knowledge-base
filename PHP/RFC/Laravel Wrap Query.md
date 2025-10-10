
when we build query, it is simple `select id, name, ... from order by` and what evs.

But sometimes we use complex function calls in fields list, and we can't filter by this values (if not to duplicate this complex functions in where's.
Moreover, in simple sql we can't group grouped results except wrap in another query.

We need some way to '->wrapOut()' which will return query builder `select * from (select your_subquery_here)`. Thus you can use builder to do all your orders, groups one more level upper.

The problem is demonstrated below (this will call function `test_result_in_percents` two times on all selected records):

```
select `test_results`.*, test_result_in_percents(test_results.id) as result_percents
from `test_results`
where test_result_in_percents(test_results.id) <= 74.91
  and `test_results`.`test_id` = 123
order by `test_results`.`id` desc;
```

When such a function (or subquery) is the main bottlenack, time increases about 2 times.


Solution is here:

```
select * from (
                  select `test_results`.*, test_result_in_percents(test_results.id) as result_percents
                  from `test_results`
                  where `test_results`.`test_id` = 123
                  order by `test_results`.`id` desc
              ) sub
where sub.result_percents <= 74.91;
```



Implementation:

```php

    /**
     * @param  string|null  $as
     *
     * @return self
     */
    public function wrapOut(string $as = null)
    {
        $as = $as ?? Str::random(12);

        $inner = clone $this;
        $this->resetPropertiesToDefault();

        return $this->fromSub($inner, $as);
    }

    private function resetPropertiesToDefault()
    {
        $blankInstance = $this->newQuery();
        $reflBlankInstance = new \ReflectionClass($blankInstance);
        foreach ($reflBlankInstance->getProperties() as $prop) {

            if ($prop->isStatic()) {
                continue;
            }

            $prop->setAccessible(true);

            $this->{$prop->name} = $prop->getValue($blankInstance);
        }
    }

```


