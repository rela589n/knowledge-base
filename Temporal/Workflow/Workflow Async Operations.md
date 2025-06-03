---
aliases:
  - Async Workflow Operations
---

[[SAGA]] compensations should be executed with `Workflow::asyncDetached` (see the [[Compensation is not executed during Cancellation|reason]]):

```php
// @@
} catch (Exception $e) {
    yield Workflow::asyncDetached(
        fn () => yield $this->videoProcessing->cancel($id),
    );

    throw $e;
}
```

`Workflow::async()` should always `yield` inside (see the [[CanceledFailure exception is never thrown when using Workflow Async operations|reason]]):

```php
$p = Workflow::async(fn () => yield $this->activity->call($params));
```
