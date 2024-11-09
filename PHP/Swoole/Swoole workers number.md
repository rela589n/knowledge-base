[[Swoole configurations]]

Number of php processses to create.

By default, `2 * CPU`. This is a reasonable default, since with [[Shared-memory processing model]] one worker process would consume all the given resources.
