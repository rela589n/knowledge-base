---
aliases:
  - Weather Problem
---
See [problem](https://leetcode.com/problems/daily-temperatures/)

Components:
- [[Discardable]]
- [[Delayed Computation]]

Solution uses [[Monotonic Queue|Monotonic Stack]] to keep track of the best applicable temperatures for the future:

```php
public function dailyTemperatures(array $temperatures): array
{
    // [73,74,75,71,69,72,76,73]
    //  73,74
    //     74,75
    //        75, _, _, _,76
    //           71, _ 72,
    //              69,72
    //                 72,76
    //                    76,_

    // What if we traverse from end to start to keep track
    // of where each particular temperature could be the result of?

    // [73,74,75,71,69,72,76,73]
    //                      [73]
    //                    76 discard [73], as it's less than 76, result = -1
    //                       queue: [76]
    //                 72 - result = 76, as it's first greater
    //                      queue: [72,76]
    //              69   - result = 72, as it's first that's greater
    //                      queue: [69, 72, 76]
    //           71      - result: 72; discard 69, as it won't participate in the equation
    //                     queue: [71, 72, 76]
    //        75         - result: 76, discard the rest, they won't participate in equation
    //                     queue: [75, 76]
    //     74            - result: 75
    //                     queue: [74, 75, 76]
    //  73               - result: 74 (first greater)
    //                     queue: [73]

    $stack = new SplDoublyLinkedList();

    $results = [];

    foreach (array_reverse($temperatures, true) as $day => $temperature) {
        while (!$stack->isEmpty()) {
            [$nextGreaterTemperature, $nextGreaterTemperatureDay] = $stack->bottom();

            if ($temperature < $nextGreaterTemperature) {
                break;
            }

            $stack->shift();
        }

        if (!$stack->isEmpty()) {
            /** @noinspection PhpUndefinedVariableInspection */
            $results[] = $nextGreaterTemperatureDay - $day;
        } else {
            // no solution for current temperature

            $results[] = 0;
        }

        $stack->unshift([$temperature, $day]);
    }

    return array_reverse($results);
}
```

Better solution [[Delayed Computation|delays computation]], and is more clear:

```php
public function dailyTemperatures(array $temperatures): array
{
    // [73,74,75,71,69,72,76,73]
    // [73] - stack
    //    74 - solution to 73, drop 73 from stack
    //    [74] - push 74 to stack
    //       75 - solution to 74, drop 74 from stack
    //       [75] - push 75 to stack
    //       [75,71] - push 71 to the stack
    //       [75,71,69] - push 69 to the stack
    //                 72 - solution to 69, and to 71
    //       [75,      72] - add 72
    //                     76 - solution to both 75, 72
    //                    [76] - add 76 to stack
    //                    [76,73] - add 73 to the stack

    $pendingBetterWeatherDays = new SplStack();

    $n = count($temperatures);
    $results = array_fill(0, $n, 0);

    foreach ($temperatures as $day => $dayTemperature) {
        while (!$pendingBetterWeatherDays->isEmpty()) {
            $pendingBetterWeatherDay = $pendingBetterWeatherDays->top();

            if ($dayTemperature <= $temperatures[$pendingBetterWeatherDay]) {
                // Current weather is no better.
                // No point looking further, as previous values have only higher expectations.
                break;
            }

            // Weather for that day can be improved by this day.
            $results[$pendingBetterWeatherDay] = $day - $pendingBetterWeatherDay;
            $pendingBetterWeatherDays->pop();
        }

        $pendingBetterWeatherDays->push($day);
    }

    return $results;
}
```

