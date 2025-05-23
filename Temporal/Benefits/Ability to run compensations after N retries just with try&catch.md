When there had already been N retries for activity call, the exception is thrown so that you can run compensations.

```php
$flightReservationId = yield $this->bookFlight($id);

try {
    $hotelReservationId = yield $this->bookHotel($id);
} catch (Exception $e) {
    yield $this->cancelFlight($flightReservationId);

    throw $e;
}

return [$flightReservationId, $hotelReservationId];
```

It also fails if time-out happens.