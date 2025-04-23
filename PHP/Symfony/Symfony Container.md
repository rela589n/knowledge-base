#### Anonymous services

It is possible to define **anonymous services** via `!service`. This may be used for factory classes, since usually we don't need to have factory as a standalone service.

#### Aliases & Binding

Define alias: `App\Util\TransformerInterface: '@App\Util\Rot13Transformer'`

It is possible to declare `bind` under `services` section. It will define bindings, which will be used in any services file.

```
App\Util\TransformerInterface $shoutyTransformer: '@App\Util\UppercaseTransformer'
App\Util\TransformerInterface: '@App\Util\Rot13Transformer'
```

