[[Activity]] [[Backward Compatibility]]

When new activity code reads data, provided by an older workflow run.

For example, if you had:
```php
yield $this->signActivity->process($id, $password);
```

And you changed it to:

```php
yield $this->signActivity->process($command);
```

After the [[Workflow Execution]] had passed this line, there's no way to revert. [[Event History]] will have `[$id, $password]` as payload.

Thus, if your want to create compatible change for parameters of method signature:

```php
#[ActivityMethod]
public function sign(string $documentId, string $password): string
```

Into this:
```php
public function sign(SignDocumentCommand $command): string
```

You can't just blindly do it, since it will cause [[Activity Execution Failure]] due to incompatible arguments.

What you do need to do, is to ensure compatibility by yourself:

```php
#[ActivityMethod]
public function sign(
  SignDocumentCommand|string $commandOrDocumentId,
  ?string $password = null
): string {
  if ($password !== null) {
    Assert::string($commandOrDocumentId);

    $command = new SignDocumentCommand($commandOrDocumentId, $password);
  } else {
    Assert::isInstanceOf($commandOrDocumentId, SignDocumentCommand::class);
    $command = $commandOrDocumentId;
  }
```

Thank God [[Workflow Replay]] doesn't fail even though new acutal activity invocation technically has a different set of parameters than was the case with the previous version.

