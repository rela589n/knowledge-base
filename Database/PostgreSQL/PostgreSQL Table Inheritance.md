---
aliases:
  - Table Inheritance
---
[[PostgreSQL]] supports such feature as table inheritance.

> Beware that if your abstract table declares ID, and you insert values only into concrete tables, you won't be able to reference abstract table's id as the foreign key (nothing there).
> > `[23503]` ERROR: insert or update on table "warehouses" violates foreign key constraint "warehouses_city_id_fkey" 
> > Detail: Key (city_id)=(a001d0d1-93d9-7178-a73d-e1b629e13242) is not present in table "cities".

> Beware that [[Primary Key|Primary Keys]] and [[Unique Constraint|Unique Constraints]] are not globally unique any longer, neither do they or  [[Foreign Key|Foreign Keys]]  propagate to the derived tables (see [caveats](https://www.postgresql.org/docs/current/ddl-inherit.html#DDL-INHERIT-CAVEATS)).

Use [[Partitioning Test]] instead.

One table inherits columns of another table, and when we insert values into that concrete table, they show up when selected from an abstract table.

This example shows that we could insert values into inherited table, and they will appear in the base table.

Also, updates to the abstract table are propagated to the inherited tables as well.

If we delete the concrete table, selects made to the abstract table will stop returning these values.

```sql
CREATE TABLE cities
(
    name       text,
    population real,
    elevation  int -- (in ft)
);

INSERT INTO cities (name, population, elevation)
VALUES ('Denver', 715522, 5280);
INSERT INTO cities (name, population, elevation)
VALUES ('Los Angeles', 3979576, 305);
INSERT INTO cities (name, population, elevation)
VALUES ('New York', 8419600, 33);

SELECT *
FROM cities;

CREATE TABLE capitals
(
    state char(2) UNIQUE NOT NULL
) INHERITS (cities);

INSERT INTO capitals (name, population, elevation, state)
VALUES ('Austin', 964254, 489, 'TX');

INSERT INTO capitals (name, population, elevation, state)
VALUES ('Boston', 692600, 141, 'MA');

INSERT INTO capitals (name, population, elevation, state)
VALUES ('Phoenix', 1680992, 1085, 'AZ');

SELECT *
FROM capitals;

ALTER TABLE cities ADD COLUMN area real;

SELECT *
FROM cities;

SELECT *
FROM capitals;

UPDATE cities SET area = 251.5 WHERE name = 'Austin';
UPDATE cities SET area = 89.6 WHERE name = 'Boston';
UPDATE cities SET area = 517.6 WHERE name = 'Phoenix';

SELECT *
FROM capitals;

UPDATE cities SET area = 154.9 WHERE name = 'Denver';
UPDATE cities SET area = 468.7 WHERE name = 'Los Angeles';
UPDATE cities SET area = 302.6 WHERE name = 'New York';

SELECT *
FROM cities;
```