## FIRST Testing principles:

- Fast - quick check that everything right when you are in development process and check whether it break something while deploy
- Isolated - the result of test should not be influenced by some other conditions. In other words, tests should be self-sufficient. One test produces one logical outcome.
- Repeatable - running the same test without code changes will always give the same result (pass or fail) independently of environment. Even when you're on the board of plane, your tests should pass successfully
- Self-validating - test must assert something, thus you should not validate test results manually
- Thorough - should cover all happy paths, all edge cases, all invalid arguments, all cases when you think the unit would fail.

