```yaml
parameters:
    app_logging.gelf.stream_link: '%env(APP_GELF_STREAM_SCHEME)%://%env(APP_GELF_HOST)%/streams/%env(APP_GELF_STREAM_ID)%'
    env(APP_GELF_STREAM_SCHEME): 'https'
    env(APP_GELF_HOST): ''
    env(APP_GELF_PORT): '12201'
    env(APP_GELF_CHUNK_SIZE): '1420'

services:
    _defaults:
        autowire: true
        autoconfigure: true

    app_logging.gelf.publisher:
        class: Gelf\Publisher
        arguments: [ '@app_logging.gelf.transport' ]

    app_logging.gelf.transport:
        class: Gelf\Transport\UdpTransport
        arguments: [ '%env(APP_GELF_HOST)%', '%env(APP_GELF_PORT)%', '%env(APP_GELF_CHUNK_SIZE)%' ]

    app_logging.gelf.formatter:
        class: App\Support\Logging\Formatter\TaggedMessageFormatter
        arguments: [ '@monolog.formatter.gelf_message', '%env(APP_GELF_TAG)%' ]
```

And tagged message formatter:

```php
final readonly class TaggedMessageFormatter implements FormatterInterface
{
    public function __construct(
        private FormatterInterface $wrappedFormatter,
        private string $tag,
    ) {
    }

    public function format(LogRecord $record): Message
    {
        /** @var Message $message */
        $message = $this->wrappedFormatter->format($record);

        $message->setAdditional('tag', $this->tag);

        return $message;
    }

    public function formatBatch(array $records): array
    {
        /** @var LogRecord $record */
        foreach ($records as $key => $record) {
            $records[$key] = $this->format($record);
        }

        return $records;
    }
}
```

To verify that logs appear you could use console command that logs test message: `$this->logger->error('test');`
