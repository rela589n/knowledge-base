[[Entity]] ***ID must be immutable***. If it is set of attributes, watch out for particular attribute updates.

Sometimes generated ID is of user's interest. For instance, tracking number.

Every ***ID must be unique*** across the system. It makes sense using *DB constraint* for every identifier. If seat is identified by row and column, (row+column) pair must be unique.

