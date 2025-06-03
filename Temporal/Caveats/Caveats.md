
[[Compensation is executed before Activity actually Completes]]

### Method names

Method names are important.

For example if activity method was named `getQuoteOfTheDay`, and worker started with it, then client code must use the same method name. If it uses another, it will result in failure.

### [[Activity Backward Compatibility]] & [[Activity Forward Compatibility]]

When new value is added to the enum, it'll not be possible to create it automatically unless workers are restarted.
