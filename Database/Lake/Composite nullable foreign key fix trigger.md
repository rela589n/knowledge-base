If null-field in the target table will actually become not-null (e.g. updated to some value), then it will not be updated back in the source table by the [[Composite foreign key]].

In order to fix that, it's necessary to add trigger function:
```sql
CREATE OR REPLACE FUNCTION app_product_update_materialized_path()
    RETURNS TRIGGER AS
$$
BEGIN
    UPDATE product
    SET category_materialized_path = new.materialized_path
    WHERE product.category_id = new.id;
    RETURN new;
END;
$$ LANGUAGE plpgsql;
```

Attach trigger to the table:

```sql
DROP TRIGGER IF EXISTS product_materialized_path_trigger ON category;
CREATE TRIGGER product_materialized_path_trigger
    AFTER UPDATE ON category
    FOR EACH ROW
    WHEN ((old.materialized_path IS NULL) AND new.materialized_path IS NOT NULL)
EXECUTE PROCEDURE app_product_update_materialized_path();
```