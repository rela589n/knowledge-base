[[Predicate]] `A -> B` means that `A` implies `B`, 
so that if `A` is `true`, then `B` is also `true`. 

![[Implication.png]]

```php
function implication(bool $a, bool $b): bool
{
    return ($a === true) <= ($b === true);
    // or 
    // return !$a || $b;
}
```

Implication is for example, `Raining => Cloudy` (if it's raining then it's cloudy).
If it's Raining, but not Cloudy, then it could not be Raining. 
It's not both Raining and not Cloudy (`~[Raining & ~Cloudy]`.

This `implication` function states if `A implies B`.

If `A` is `false`, then it's always `true`, because `A` would have implied `B` if it were `true`.

If `A` is `true`, then it's result of `B` - because since `A` is satisfied, it must imply that `B` has been satisfied as well.


