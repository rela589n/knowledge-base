---
aliases:
  - Generator-based evaluation
  - Cooperative multitasking
---
See [article](https://www.npopov.com/2012/12/22/Cooperative-multitasking-using-coroutines-in-PHP.html)

Basically, code looks like this:

```php
<?php

$fiveEightNine = evaluate(fiveEightNine());

var_dump($fiveEightNine);

function fiveEightNine(): \Generator
{
    $fiveSevenNine = yield fiveSevenNine();

    return $fiveSevenNine + 10;
}

function fiveSevenNine(): Generator
{
    $oneTwoThree = yield oneTwoThree();

    $fourFiveSix = yield fourFiveSix();

    return $oneTwoThree + $fourFiveSix;
}

function oneTwoThree(): Generator
{
    return yield 123;
}

function fourFiveSix(): Generator
{
    return yield 456;
}
```

It suffers from [[Red-blue function problem]], yet for a long time it's what [[Temporal]] has been using.

Evaluation is pretty simple. On every step it just sends to the generator each value as "evaluated". Thus, if there were "inner generators", these are evaluated first, and then return value is substituted in place so that `yield` acts as `await` in this case:

```php
function evaluate(Generator $code): mixed
{
    // for some reason it's just not possible
    // to implement the same with foreach over generator
    do {
        $statement = $code->current();

        if ($statement instanceof Generator) {
            $value = evaluate($statement);
        } else {
            $value = $statement;
        }
    } while (null !== $code->send($value));

    return $code->getReturn();
}
```


