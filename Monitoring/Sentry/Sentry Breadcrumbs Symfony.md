```yaml
monolog:
  handlers:
    sentry_breadcrumbs:
      type: service
      id: App\BreadcrumbsHandler
```

```php
use Monolog\Handler\AbstractProcessingHandler;
use Monolog\Level;
use Monolog\LogRecord;
use Sentry\Breadcrumb;
use Sentry\State\HubInterface;
use Sentry\State\Scope;

use function array_is_list;

final class BreadcrumbsHandler extends AbstractProcessingHandler
{
    private const array LEVELS = [
        Level::Debug->value => Breadcrumb::LEVEL_DEBUG,
        Level::Info->value => Breadcrumb::LEVEL_INFO,
        Level::Notice->value => Breadcrumb::LEVEL_INFO,
        Level::Warning->value => Breadcrumb::LEVEL_WARNING,
        Level::Error->value => Breadcrumb::LEVEL_ERROR,
        Level::Critical->value => Breadcrumb::LEVEL_FATAL,
        Level::Alert->value => Breadcrumb::LEVEL_FATAL,
        Level::Emergency->value => Breadcrumb::LEVEL_FATAL,
    ];

    public function __construct(
        private readonly HubInterface $hub,
    ) {
        parent::__construct();
    }

    protected function write(LogRecord $record): void
    {
        $this->hub->configureScope(function (Scope $scope) use ($record): void {
            $scope->addBreadcrumb(
                new Breadcrumb(
                    $this->convertMonologLevelToSentryLevel($record->level),
                    Breadcrumb::TYPE_DEFAULT,
                    $record->channel,
                    $record->message,
                    $this->processContext($record->context),
                    (float)$record->datetime->format('U.u'),
                ),
            );
        });
    }

    private function processContext(array $context): array
    {
        if ([] === $context) {
            return $context;
        }

        if (array_is_list($context)) {
            return ['ctx' => $context];
        }

        return $context;
    }

    private function convertMonologLevelToSentryLevel(Level $level): string
    {
        /** @psalm-suppress UndefinedConstant */

        return self::LEVELS[$level->value] ?? Breadcrumb::LEVEL_FATAL;
    }
}
```

