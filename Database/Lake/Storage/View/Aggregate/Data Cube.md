---
aliases:
  - OLAP Cube
---
**Data Cube** - special case of [[Materialized View]]. 
Aggregates grid grouped by different dimensions. 

Each cell contains aggregate (e.g. SUM) of given attribute (e.g. net_price) for given dimensions (e.g. products, dates) in facts table (e.g. sales).

Data Cubes allow not only get aggregates by combination of dimensions, but also find aggregation by any dimension.

> Advantage of Data Cubes is that some queries become really fast. To get aggreate of yesterday's sales - no longer need to scan over millions of records.

> Disadvantage of Data Cubes is that we have no such flexibility as when having raw data. Finding proportion of items having price greater than 100$ by yesterday is not possible using data cube.

