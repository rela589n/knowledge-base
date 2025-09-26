Since **Schema Updates** in [[PostgreSQL]] are **[[Transaction|Transactional]]**, you can create Schema per tenant.

This is a valid SQL:

```sql
CREATE SCHEMA tenant1;
CREATE SCHEMA tenant2;

BEGIN;

CREATE TABLE tenant1.products
(
    name VARCHAR(100) NOT NULL PRIMARY KEY
);

INSERT INTO tenant1.products (name)
VALUES ('Laptop'),
       ('Smartphone'),
       ('Headphones');

CREATE TABLE tenant2.products
(
    name VARCHAR(100) NOT NULL PRIMARY KEY
);

INSERT INTO tenant2.products (name)
VALUES ('Laptop'),
       ('Smartphone'),
       ('Headphones');
COMMIT;
```
