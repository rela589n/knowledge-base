Serializer doesn't analyse `@var` annotation:

```diff
+    /** @param array<array-key,Item> $items */
     public function __construct(
         private string $code,
-        /** @var Item[] */
         private array $items,
     ) {
         $this->id = Uuid::fromBase58($this->code);
@@ -26,7 +26,7 @@ 
```