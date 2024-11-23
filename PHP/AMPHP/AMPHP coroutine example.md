[[AMPHP]]

Consider that we integrate our application with some kind of slow third-party api. Let's say, we are building e-commerce platform that has to integrate erp api to get the product prices.

Yet, it turns out to be that erp doesn't provide a way to get the full list by given ids. Unfortunately, we can only get the price for any particular product, but not for all of them at the same time.

```php
final class PriceGateway
{
    public function __construct(
        private HttpClient $httpClient,
    ) {
    }

    public function getPrice(string $productId): Price
    {
        $response = $this->httpClient->request('GET', '/api/product-price', [
            'query' => [
                'productId' => $productId,
            ],
        ]);

        $resultPrice = $response->getJsonArray();

        return new Price($resultPrice['currency'], $resultPrice['unitAmount']);
    }
}
```


Yet, it is still possible to get the list of prices by product ids without having to wait for all the requests one by one:

```php
final class PricesConcurrentGateway
{
    private const CHUNK_SIZE = 64;

    public function __construct(
        private PriceGateway $gateway,
    ) {
    }

    /**
     * @param list<string> $productIds
     *
     * @return Price[]
     */
    public function getPrices(array $productIds): array
    {
        /** @var Price[][] $prices */
        $prices = [];

        foreach (array_chunk($productIds, self::CHUNK_SIZE) as $productIdsChunk) {
            $promises = array_map(
                fn ($productId) => async($this->gateway->getPrice($productId)),
                $productIdsChunk,
            );

            $prices[] = awaitAll($promises);
        }

        return array_merge(...$prices);
    }
}
```

This `PricesConcurrentGateway` makes at most 64 concurrent requests to the third-party api in order to get the the prices data one by one.



