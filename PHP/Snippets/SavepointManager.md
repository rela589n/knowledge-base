---
aliases:
  - Savepoint Transaction
---
Usage:

```php
try {
    $this->savepointManager->savepointTransaction(
        // might use multiple steps
        fn () => $this->settleFinances($id),
    );
} catch (\Throwable $e) {
    // Doctrine closed the EntityManager on its way out, and a fresh one still
    // speaks to the same connection - so the reversal can be recorded after all.
    $this->managerRegistry->resetManager();

    // might use multiple steps
    $this->revertFinances($id);

    throw $e;
}
```

Each step then uses `savepoint()` method:

```php
$this->savepointManager
    ->savepoint(function () use ($transaction): void {
        if ($transaction->isSettled()) {
            return;
        }

        $this->gateway->settle($transaction);
        $transaction->settled();

        $this->entityManager->flush();
    });
```

The manager itself:
```php
final readonly class SavepointManager
{
    public function __construct(
        private EntityManagerInterface $entityManager,
    ) {
    }

    /**
     * @template T
     *
     * @param \Closure(): T $func
     *
     * @return T
     */
    public function savepointTransaction(\Closure $func): mixed
    {
        // Start the outer transaction
        $this->entityManager->beginTransaction();

        try {
            // Entity Manger starts the initial savepoint, and rolls back to the last savepoint.
            return $this->entityManager->wrapInTransaction($func);
        } finally {
            // Commit must run on both paths:
            // 1. on failure, the client's rollback() has already rewound to the last savepoint,
            // 2. on success, the savepoint was merely released
            $this->entityManager->getConnection()->commit();
        }
    }

    /**
     * @template T
     *
     * @param \Closure(): T $func
     *
     * @return T
     */
    public function savepoint(\Closure $func): mixed
    {
        /** Not doing rollback() here, since {@see EntityManagerInterface::wrapInTransaction()} rolls back. */
        $result = $func();

        $this->updateSavepoint();

        return $result;
    }

    private function updateSavepoint(): void
    {
        if (!$this->entityManager->getConnection()->isTransactionActive()) {
            throw TransactionRequiredException::transactionRequired();
        }

        // Release the last savepoint
        $this->entityManager->getConnection()->commit();

        // Start savepoint anew
        $this->entityManager->beginTransaction();
    }
}
```