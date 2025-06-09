Since [[Value Objects have no identity]], it makes no sense to have bidirectional associations for the value objects. 

Value object should not hold reference to the parent that owns itself.

If you are tempted to do so, rethink maybe it has identity and should really be an [[Entity]].