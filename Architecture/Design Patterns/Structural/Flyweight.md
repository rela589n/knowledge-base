Let us to **reduce the memory usage**.

It suggests to determine the **intrinsic** (immutable, readonly) and **extrinsic** states of the object and split them, **leaving objects only with intrinsic state**. 

Doing so, we would decrease the overall number of duplicated information (**intrinsic** will be shared via single object).

This is an implementation options only for [[Value Object|Value Objects]], but not for [[Entity|Entities]].
