---
aliases:
  - Async Workflow Operations
---

[[SAGA]] compensations should be executed with `Workflow::asyncDetached`:

```php
// @@
} catch (Exception $e) {
    yield Workflow::asyncDetached(
        fn () => $this->videoProcessing->cancel($id),
    );

    throw $e;
}
```

