[[PostgreSQL TSVector]]

```php
final class Version2032000000000 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Add product search vector column, index, function and triggers';
    }

    public function up(Schema $schema): void
    {
        $this->addSql("ALTER TABLE products ADD search_vector TSVECTOR NOT NULL DEFAULT ''::TSVECTOR");
        $this->addSql('ALTER TABLE products ALTER search_vector DROP DEFAULT');

        $this->addSql('CREATE INDEX products_search_vector_idx ON products USING GIN (search_vector)');

        $highest = SearchWeight::HIGHEST;
        $medium = SearchWeight::MEDIUM;
        $low = SearchWeight::LOW;
        $lowest = SearchWeight::LOWEST;

        $this->addSql(<<<SQL
            CREATE OR REPLACE FUNCTION build_product_search_vector(product products)
            RETURNS tsvector AS \$\$
            BEGIN
                RETURN
                    SETWEIGHT(TO_TSVECTOR('simple', COALESCE(product.sku, '')), '$highest') ||
                    SETWEIGHT(TO_TSVECTOR('simple', COALESCE(product.title, '')), '$medium') ||
                    SETWEIGHT(TO_TSVECTOR('simple', COALESCE(product.description, '')), '$medium') ||
                    SETWEIGHT(TO_TSVECTOR('simple', COALESCE(
                        (SELECT name FROM categories WHERE id = product.category_id), ''
                    )), '$low') ||
                    SETWEIGHT(TO_TSVECTOR('simple', COALESCE(product.brand, '')), '$lowest');
            END;
            \$\$ LANGUAGE plpgsql
            SQL);

        $this->addSql(<<<'SQL'
            CREATE OR REPLACE FUNCTION products_search_vector_trigger_fn() RETURNS trigger AS $$
            BEGIN
                NEW.search_vector := build_product_search_vector(NEW);
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql
            SQL);

        $this->addSql(<<<'SQL'
            CREATE TRIGGER products_search_vector_trigger
                BEFORE INSERT OR UPDATE OF sku, title, description, category_id, brand
                ON products
                FOR EACH ROW
                EXECUTE FUNCTION products_search_vector_trigger_fn()
            SQL);

        $this->addSql(<<<'SQL'
            CREATE OR REPLACE FUNCTION categories_products_search_vector_trigger_fn() RETURNS trigger AS $$
            BEGIN
                IF OLD.name IS DISTINCT FROM NEW.name THEN
                    UPDATE products
                    SET search_vector = build_product_search_vector(products.*)
                    WHERE category_id = NEW.id;
                END IF;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql
            SQL);

        $this->addSql(<<<'SQL'
            CREATE TRIGGER categories_products_search_vector_trigger
                AFTER UPDATE OF name
                ON categories
                FOR EACH ROW
                EXECUTE FUNCTION categories_products_search_vector_trigger_fn()
            SQL);
    }

    public function postUp(Schema $schema): void
    {
        parent::postUp($schema);

        $searchVectorService = new ProductSearchVectorReindexService($this->connection);
        $searchVectorService->reindexAll();
    }

    public function down(Schema $schema): void
    {
        $this->addSql('DROP TRIGGER IF EXISTS categories_products_search_vector_trigger ON categories');
        $this->addSql('DROP FUNCTION IF EXISTS categories_products_search_vector_trigger_fn()');
        $this->addSql('DROP TRIGGER IF EXISTS products_search_vector_trigger ON products');
        $this->addSql('DROP FUNCTION IF EXISTS products_search_vector_trigger_fn()');
        $this->addSql('DROP FUNCTION IF EXISTS build_product_search_vector(products)');

        $this->addSql('DROP INDEX products_search_vector_idx');
        $this->addSql('ALTER TABLE products DROP search_vector');
    }
}
```