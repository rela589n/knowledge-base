
Given that max USN is 7.

- `previous_usn=6` and `current_usn=5`, - this update should be considered lost.
- `previous_usn=6` and `current_usn=1`, - this update should be considered valid, since the overflow happened
- `previous_usn=1` and `current_usn=6` - this update should be considered lost, since the overflow happened
- `previous_usn=1` and `current_usn=2` - this update should be considered valid, as the basic case.

Working approach:

```php
public function greaterThan(int $number): bool
{
    return ($this->number - $number + self::SIZE) % self::SIZE < self::HALF_SIZE;
}
```

![[Modulos.png]]

In this code, `+ self::SIZE` is necessary due to the fact that we'll get negative numbers when subtracting, but we'd like our modulo to be just less than half size (e.g. `0` to `half size`).