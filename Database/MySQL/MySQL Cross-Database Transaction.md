It's similar to what [[PostgreSQL Schema-per-Tenant]] example showed.

```sql
CREATE DATABASE tenant1;
CREATE DATABASE tenant2;

USE tenant1;
CREATE TABLE products
(
    name VARCHAR(100) NOT NULL PRIMARY KEY
) ENGINE=InnoDB;

USE tenant2;
CREATE TABLE products
(
    name VARCHAR(100) NOT NULL PRIMARY KEY
) ENGINE=InnoDB;

START TRANSACTION;

INSERT INTO tenant1.products (name)
VALUES ('Laptop'),
       ('Smartphone'),
       ('Headphones');

INSERT INTO tenant2.products (name)
VALUES ('Laptop'),
       ('Smartphone'),
       ('Headphones');

COMMIT;
```