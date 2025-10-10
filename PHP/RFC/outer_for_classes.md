```

    public static function castUsing(array $arguments)
    {
        return new class implements CastsAttributes {

            public function get($model, string $key, $value, array $attributes): outer
            {
                return new outer($value);
            }

            public function set($model, string $key, $value, array $attributes)
            {
                // TODO: Implement set() method.
            }
        };
    }
```

$outer as well

```

```
