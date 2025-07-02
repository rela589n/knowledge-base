Let us to **reduce the memory usage**.

It suggests to determine the **intrinsic** ([[Immutability|Immutable]], readonly) and **extrinsic** states of the object and split them, **leaving objects only with intrinsic state**. 

Doing so, we would decrease the overall number of duplicated information (**intrinsic** will be shared via single object).

This is an implementation option only for [[Value Object|Value Objects]] (like electrical outlets), but not for [[Entity|Entities]].

