Since **Schema Updates** in [[PostgreSQL]] are **[[Transaction|Transactional]]**, you can create Schema per tenant.

This is a valid SQL:

```sql
CREATE SCHEMA tenant1;
CREATE SCHEMA tenant2;

BEGIN;

SET search_path = tenant1;

CREATE TABLE products
(
    name VARCHAR(100) NOT NULL PRIMARY KEY
);

INSERT INTO products (name)
VALUES ('Laptop'),
       ('Smartphone'),
       ('Headphones');

SET search_path = tenant2;

CREATE TABLE products
(
    name VARCHAR(100) NOT NULL PRIMARY KEY
);

INSERT INTO products (name)
VALUES ('Laptop'),
       ('Smartphone'),
       ('Headphones');

COMMIT;
```
