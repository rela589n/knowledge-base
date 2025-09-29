## Tests are design tools. 

You can detect whether good or bad design is by means of testing. 
From other hand, TDD promotes us to write better code.

## Repeatability

> Unstable dependencies hurt repeatability of tests.
> Implicit dependencies hurt our reasoning about code.
> Unstable implicit dependencies hurt our sanity.

Such a dependency is system clock (new Date() or Date.today() will use it). We will almost never get the same result while testing.


## Virtual Clock - isn't an option

Just create clock interface implemented by wrapper which uses system clock and your test clock.
This solves repeatability problem.

But here's another problem: indirection without abstraction.
We don't hide details, but rather expose them.

> If we need indirection, it should be smallest possible. And we must introduce better abstraction.

Virtual Clock is an "artificial" abstraction, which increases congnitive load.

> Don't inject what you can ignore

When we need just number representing timestamp, why do we inject object which gives us timestamp. 
We should demand direct value which we need.
Thus, we'd better use parameter instead of clock.
And for current time we can use decorator.


## Summing up

> Write code which is more independent of context. It will become more testable, reusable, easy to understand and maintain.


