```php
$expressionBuilder = Criteria::expr();

$criteria = new Criteria();
$criteria->where($expressionBuilder->eq('name', 'jwage'));
$criteria->orWhere($expressionBuilder->eq('name', 'romanb'));

$collection->matching($criteria);
```
