From api point return `StreamedResponse`:

```php
return new StreamedResponse(
    static fn (): int => fpassthru($fileStreamDto->stream),
    headers: [
        'Content-Type' => $fileStreamDto->mimeType,
        'Content-Length' => $fileStreamDto->fileSize,
        'Content-Disposition' => HeaderUtils::makeDisposition(
            HeaderUtils::DISPOSITION_ATTACHMENT,
            $fileStreamDto->baseName,
            $notificationCampaign->getId()->toRfc4122(),
        ),
    ],
);
```