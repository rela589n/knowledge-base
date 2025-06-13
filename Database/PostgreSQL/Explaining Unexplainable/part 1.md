# Explaining the unexplainable

```
                                                        QUERY PLAN
---------------------------------------------------------------------------------------------------------------------------
 Sort  (cost=146.63..148.65 rows=808 width=138) (actual time=55.009..55.012 rows=71 loops=1)
   Sort Key: n.nspname, p.proname, (pg_get_function_arguments(p.oid))
   Sort Method: quicksort  Memory: 43kB
   ->  Hash Join  (cost=1.14..107.61 rows=808 width=138) (actual time=42.495..54.854 rows=71 loops=1)
         Hash Cond: (p.pronamespace = n.oid)
         ->  Seq Scan on pg_proc p  (cost=0.00..89.30 rows=808 width=78) (actual time=0.052..53.465 rows=2402 loops=1)
               Filter: pg_function_is_visible(oid)
         ->  Hash  (cost=1.09..1.09 rows=4 width=68) (actual time=0.011..0.011 rows=4 loops=1)
               Buckets: 1024  Batches: 1  Memory Usage: 1kB
               ->  Seq Scan on pg_namespace n  (cost=0.00..1.09 rows=4 width=68) (actual time=0.005..0.007 rows=4 loops=1)
                     Filter: ((nspname <> 'pg_catalog'::name) AND (nspname <> 'information_schema'::name))
```

[[PostgreSQL]] stores **stats about the data**. It knows how many distinct values, how many rows there are, which are the most common values, etc.

**Cost** - is the relative metric to measure **time and resources usage**. Cost of fetching single page sequentially is equal to `1.0`.

There are cost configurations:
- `seq_page_cost=1.0`;
- `random_page_cost=4.0`;
- `cpu_tuple_cost=0.01`.

Planner up to some point **examines all possible plans** to run the query.

## Examine different plans

Just for a testing, we can `SET enable_<option>=false;` in order to see what other plan [[PostgreSQL]] can choose.

`set enable_indexscan = false;` will disable index scan;
`set enable_bitmapscan = false;` will disable bitmap scan.

Full list is available:
```sql
select name, setting, short_desc || coalesce(E'\n' || extra_desc, '')
from pg_settings where name ~ '^enable_';
```


## Costs

There are **two costs** number..number. 

**First number** is the cost for the **first row** selection including **preparations** (like sorting data etc).

**Second number** - cost to get **all matching rows**.

**Query plan decision** is made based on the **second one**.

## Rows & Width

**Rows number** is the metric, which shows **how many rows** query is possibly capable of returning. This metric is really **important for joins**.

**Width** is the metric, which shows **how many bytes** of data, on average, **each row will hold**. The less fields we select, the less is the width.

## Explain Structure

Each explain is **the tree** - upper node requires data from the lower node.

Some operations **return data gradually** during the operation execution (seq scan for instance), while others need to **process all the data beforehand** (hash for instance).

> Gradual operations are like `yield` operator (generator) in PHP

## Explain Analyze

Actually runs the query and shows additional metrics.

**Actual time** - shows two numbers (1) how much time it took **for startup**, (2) how much time it took **for returning all matching rows**. Time is measured in **milliseconds**.

**Actual rows** - how many rows **were returned** (on average).

**Loops** - how many times the operation was executed.

There may be really poor performance when loops number is big.

```
Nested Loop  (cost=0.00..10715.90 rows=26284 width=4449) (actual time=0.054..291.131 rows=26284 loops=1)
  ->  Index Scan using books_index_title on books  (cost=0.00..3306.28 rows=26284 width=3357) (actual time=0.033..50.773 rows=26284 loops=1)
  ->  Index Scan using categories_pkey on categories  (cost=0.00..0.27 rows=1 width=1092) (actual time=0.002..0.003 rows=1 loops=26284)
        Index Cond: (categories.id = books.category_id)
Total runtime: 312.212 ms
```

Even though, it is index scan, `loops=26284`, which makes total time of second index scan around 78ms.





