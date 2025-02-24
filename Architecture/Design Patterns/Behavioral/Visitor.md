Patterns that allows us to traverse [[Composite]] trees in a single class.

Example:
- dump the whole tree of filters (one class that implements visitor interface)

Visitor pattern allows to avoid creating a [[Factory]] of way too separated algorithms. 

For instance, when we would need to execute some logic which depends on polymorphic classes usually we would create service class per each type of entity as well as create factories which will check original class instance and create&return correlated service class.

Instead of this we would combine this into a single class having polymorphic methods (or if no methods overloading is supported, just methods with different names and arguments types). Ultimately there will be N methods of Visitor class instead of N classes. Having this, we define interface for visited object with single method `visit(Visitor v): ResultOfVisitor`. Each of polymorphic classes will implement method and call appropriate method of `Visitor` class.
