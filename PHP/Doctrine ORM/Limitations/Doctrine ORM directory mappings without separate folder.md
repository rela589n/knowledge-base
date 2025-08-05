Mappings relate entities by their fields. Could we use that in order to load mappings?

Currently `\Doctrine\Persistence\Mapping\Driver\ColocatedMappingDriver::getAllClassNames` includes all the files in the mapping directory, and then uses `get_declared_classes()` function in order to filter only the entities from that list.

IMO, we could set the basic namespace for bundle entities `MyBundle\Domain` and write mapping driver that would include all related classes (reflecting the properties types) starting from some aggregate root that will be specified in the configuration.

We could use [[Doctrine metadata exclude path]]