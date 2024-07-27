Strip down the entity to the ***most intrinsic attributes*** that identify it and are most commonly used to find the entity.

Look to ***move non-essential attributes*** and behavior into other objects. Attributes of the entity must be bound to it by the identity.

Entity ***ID must be immutable***. If it is set of attributes, watch out for particular attribute updates.

Sometimes generated ID is of user's interest. For instance, tracking number.

Every ***ID must be unique*** across the system. It makes sense using *DB constraint* for every identifier. If seat is identified by row and column, (row+column) pair must be unique.





