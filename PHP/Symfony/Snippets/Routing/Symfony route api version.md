`routes.yaml`:

```diff
api_module:
  resource: '../../../**/{*FrontendApiPoint.php}'
  type: attribute
- prefix: /api/v1.0
+ prefix: /api/{apiVersion}
+ requirements:
+   apiVersion: !php/const App\ApiVersion::PATTERN
+ defaults:
+   apiVersion: "%api_version%"
  host: "%api_host%"
  schemes: "%api_scheme%"
```

`services.yaml`:
```yaml
parameters:  
  api_version: 'v1.0'
```

```php
final readonly class ApiVersion
{
    public const string PATTERN = 'v\d+\.\d+';

    public function __construct(
        private float $apiVersion,
    ) {
    }

    public static function fromVersionString(string $apiVersion): self
    {
        if (!preg_match(sprintf('/%s/', self::PATTERN), $apiVersion)) { // @phpstan-ignore booleanNot.exprNotBoolean
            throw new \InvalidArgumentException(sprintf('Invalid API version "%s".', $apiVersion));
        }

        return new self((float) ltrim($apiVersion, 'v'));
    }

    public function lessThan(float $version): bool
    {
        return $this->apiVersion < $version;
    }

    public function greaterThanOrEqualTo(float $version): bool
    {
        return $this->apiVersion >= $version;
    }
}
```

Value Resolver:
```php
final readonly class ApiVersionValueResolver implements ValueResolverInterface
{
    public function resolve(Request $request, ArgumentMetadata $argument): iterable
    {
        if (!$this->supports($argument)) {
            return [];
        }

        $apiVersion = $request->attributes->get('apiVersion');

        if (!is_string($apiVersion)) {
            return [];
        }

        return [ApiVersion::fromVersionString($apiVersion)];
    }

    private function supports(ArgumentMetadata $argumentMetadata): bool
    {
        return ApiVersion::class === $argumentMetadata->getType();
    }
}
```

