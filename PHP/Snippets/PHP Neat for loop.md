```php
for ($inlineTarget = $premise->getInlineTarget(), $counter = 0;
     $inlineTarget !== null && ++$counter;
     $inlineTarget = $inlineTarget->getInlineTarget()
) {
    if ($counter >= $this->k) {
        return true;
    }
}

return false;
```
