**Correct** distributed algorithm **satisfies all its [[Distributed algorithm properties|properties]] in a [[System Models|system model]]** which it is used in.

Even though algorithm is theoretically correct in a selected [[System Models|system model]], it doesn't mean it won't face problems in practice. Other way round, harsh reality will bite your ass again and again revealing issues with failed nodes/hardware/firmware/drivers etc.

The implementation should **handle the cases which seem to be impossible** from theoretical perspective, since on practice a lot **unexpected things happen**. Throwing kind of `LogicException` is a good way to handle such issues.
