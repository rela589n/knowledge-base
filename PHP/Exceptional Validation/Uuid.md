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
    $service->process($command);
} catch (Exception $exception) {
    $violationList = $this->exceptionMapper->map($command, $exception);

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