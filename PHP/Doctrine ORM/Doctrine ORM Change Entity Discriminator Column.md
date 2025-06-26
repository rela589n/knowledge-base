---
aliases:
  - Change Entity Discriminator Column
---
It was sorted out with [[Deferrable Constraint|Deferred Constraint]].

```php
try {
    $this->importer->processItem($command);
} catch (ChangedAnswerTypeException $e) {
    /*
    * When it is necessary to change the answer type of the question (discriminator column), delete the old question, and import a new one.
    * All necessary foreing keys pointing to abstract Question table will still be preserved owing to deferred constraints.
    */
    $this->repository->deferConstraints();

	$this->entityManager->remove($e->getQuestion());  
	$this->entityManager->flush();

    // Importing once again
    $this->importer->processItem($command);
}
```

Make sure to replace existing [[Foreign Key]] constraints with [[Deferrable Constraint|Deferred]] ones.
