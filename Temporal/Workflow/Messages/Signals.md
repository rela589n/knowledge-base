Signal is async write request, that provides the ability to send some data to the [[Workflow Execution|running workflow]]. You can't await any result or error from signal method.

Annotated with `#[SignalMethod]`.

You can use `Workflow::await()` to await some condition to be met.
