**For Example:** 
We have Car ([[Aggregate Root]]) entity with four Wheels.

There's no point of querying wheel objects apart from car from the database and then checking whether they belong to that Car or not. 

It is vice versa - we query database to find Car, and then check the particular wheel of that Car.
