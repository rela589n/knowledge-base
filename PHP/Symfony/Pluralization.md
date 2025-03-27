Create file `messages+intl-icu.uk.yaml` and make sure you have `ext-intl` installed.

Then, define translation:

```yaml
calendar_days: >-
    {periodForm, select,
        0 {{periodDays} календарний день} 
        1 {{periodDays} календарних дні} 
        other {{periodDays} календарних днів}
    }
```

Then, translate it like this:

```php
/** @param positive-int $totalDays */
private function getCalendarDaysText(int $totalDays): string
{
    return $this->translator->trans('calendar_days', [
        'periodForm' => $this->getPeriodForm($totalDays),
        'periodDays' => $totalDays,
    ], locale: 'uk');
}
```

To get the correct form for `uk` language, you could use this method:
```php
/**
 * @param positive-int $totalDays
 *
 * @return int<0,2>
 */
private function getPeriodForm(int $totalDays): int
{
    $mod = $totalDays % 100;

    if ($mod > 4 && $mod < 20) {
        return 2;
    }

    $forms = [2, 0, 1, 1, 1, 2];
    $key = min($mod % 10, 5);

    return $forms[$key];
}
```

> Also, you could check out `TranslatorTrait::getPluralizationRule()` method that probably does the same, but right now is private.


