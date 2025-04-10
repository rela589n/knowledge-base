

All right, let's see it with the example.

```php
<?php

use PhPhD\ExceptionalValidation;
use PhPhD\ExceptionalValidation\Capture;

class NotEnoughMoneyException
{
}
class InvalidUuidException
{
}

#[ExceptionalValidation]
class TransferMoneyCommand
{
    public function __construct(
        #[Capture(InvalidUuidException::class)]
        #[Capture(NotEnoughMoneyException::class)]
        public readonly string $fromCardId,

        #[Capture(InvalidUuidException::class)]
        public readonly string $toCardId,
    ) {
    }
}

$command = new TransferMoneyCommand('eb27966e-b78f-7afc-96c5-cd6e18c37616', '!not valid!');

try {
    $commandBus->process($command);
} catch (ExceptionalValidationFailedException $e) {
    $violationList = $e->getViolationList();

	// This is incorrect behavior, since it was toCardId that is invalid:
    // $violationList[0].invalidValue = '!not valid!'
    // $violationList[0].propertyPath = 'fromCardId'
}


try {
    $service->process($command);
} catch (InvalidUuidException $exception) {
    if ($exception->getValue() === $command->fromCardId) {
        // we know that it happened from `fromCardId` value
    }

    if ($exception->getValue() === $command->toCardId) {
        // we know that it happened from `toCardId` value
    }
}

#[ExceptionalValidation]
class TransferMoneyCommand
{
    public function __construct(
        #[Capture(InvalidUuidException::class, condition: InvalidUuidValueMatchCondition::class)]
        #[Capture(NotEnoughMoneyException::class)]
        public readonly string $fromCardId,

        #[Capture(InvalidUuidException::class, condition: InvalidUuidValueMatchCondition::class)]
        public readonly string $toCardId,
    ) {
    }
}
```


Sorry if it's not clear right off the way.

I'll try to explain it a little more easier way.

Let's see two approaches that should lead to the same result.

First - standard validation. It looks like this:

```php
class TransferMoneyCommand
{
    #[Assert\Uuid()]
    public string $fromCardId;

    #[Assert\Uuid()]
    public string $toCardId;
}
```

Having object (`fromCardId = 'dba3ed3f-0a78-79fa-91d6-1697049dce0d'`, `toCardId = 'invalid'`) results in violation at `toCardId`.

Second approach is exceptional validation, looks like this:

```php
class TransferMoneyCommand
{
    #[Capture(InvalidUuidException::class)]
    public string $fromCardId;

    #[Capture(InvalidUuidException::class)]
    public string $toCardId;
}
```

The same object (`fromCardId = 'dba3ed3f-0a78-79fa-91d6-1697049dce0d'`, `toCardId = 'invalid'`) should in violation at `toCardId`.

Here violation is based on already thrown exception from the client code, and more explanation can be found here on the [diagram](https://github.com/phphd/exceptional-validation?tab=readme-ov-file#how-it-works-%EF%B8%8F).

TLDR, it's namely the following:

```php
// code to get property path:

try {
    // @@ $stack->next($envelope)
} catch (InvalidUuidException $exception) {
    $propertyPath = null;

    if ($exception->getValue() === $command->fromCardId) {
        $propertyPath = 'fromCardId';
    }
    if ($exception->getValue() === $command->toCardId) {
        $propertyPath = 'toCardId';
    }
    // @@ process the violation
}
```

Therefore it's not possible to know where this `InvalidUuidException` originated from unless we have value in it.

If there's `getValue()`, we can match with `fromCardId` and `toCardId` to know where it originated from.

Please, let me know this clarifies why `getValue()` is essential.


Regarding `InvalidUidException`, IMO it's better to keep them separate.

For example, assuming we use single exception, there could be edge case when there are both ulid and uuid in single place:
```php
class SomeCommand
{
    #[Capture(InvalidUidException::class)]
    public string $ulid;

    #[Capture(InvalidUidException::class)]
    public string $uuid;
}
```

If client code gets SomeCommand(`ulid=01H5Z7XQ6Y3K4J2W8V9N0M1P2A`, `uuid=01H5Z7XQ6Y3K4J2W8V9N0M1P2A`), it will result in `InvalidUidException` when creating `Uuid::fromString()`:

```php
$ulid = Ulid::fromString($command->ulid);
$uuid = Uuid::fromString($command->uuid); // throws
```

This exception should be mapped to `uuid`, as it was from this property that it originated.

Yet, since `#[Capture` attributes are the same (same classname), and properties use the same value, it will be mapped incorrectly (ascribed to `ulid`, while should've been to `uuid`).

Therefore, if possible, I would like ask keeping them as separate exceptions.
