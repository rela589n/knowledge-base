If there were already N retries for activity call, exception is thrown, and you can run compensations.

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
