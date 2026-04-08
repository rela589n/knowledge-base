
```php
#[AsEventListener(event: WorkerMessageFailedEvent::class, priority: -200)]
final readonly class WorkerMessageFailedEventListener
{
    public function __construct(
        #[Autowire('@failure.notification.bus')]
        private MessageBusInterface $failureNotificationBus,
        #[Autowire('%env(bool:FAILURE_NOTIFICATIONS_ENABLED)%')]
        private bool $isEnabled,
    ) {
    }

    public function __invoke(WorkerMessageFailedEvent $event): void
    {
        if (!$this->isEnabled) {
            return;
        }

        if ($event->willRetry()) {
            return;
        }

        $envelope = $event->getEnvelope();
        $message = $envelope->getMessage();

        $context = new FailureNotificationContext($event->getThrowable());

        $this->failureNotificationBus->dispatch($message, [new HandlerArgumentsStamp([$context])]);
    }
}
```