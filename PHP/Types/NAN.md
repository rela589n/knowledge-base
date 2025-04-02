🤔 Did You Know that PHP Has a NAN Type!

In PHP, NAN (Not A Number) is a special floating-point value returned by invalid math operations, like `sqrt(-1)`.


...code block


Also, you can't just check that `$value === NAN`, since it will always return `false` 🤯.

To check whether a `float` is `NAN`, `is_nan()` should be used.


