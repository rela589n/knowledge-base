Allows us to traverse [[Composite]] trees with a single class.

For example, we could dump the whole tree of filters (one class that implements visitor interface).

Visitor is a way to eliminate `instanceof` checks in favor of [[Polymorphism|polymorphism]].

Visitor pattern allows to avoid creating a [[Factory]] of way too separated algorithms. 

For instance, when we would need to execute some logic which depends on [[Polymorphism|polymorphic]] classes usually we would create service class per each type of entity as well as create factories which will check original class instance and create&return correlated service class.

Instead of this we would combine this into a single class having [[Polymorphism|polymorphic]] methods (one method with particular name and arguments types per each entity in hirerarchy). Ultimately there will be N methods of Visitor class instead of N classes. Having this, we define interface for visited object with single method `visit(Visitor v): ResultOfVisitor`. Each of [[Polymorphism|polymorphic]] classes will implement method and call appropriate method of `Visitor` class.
