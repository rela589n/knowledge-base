**Multi-Object [[Transaction|Transactions]]** - ***modify* multiple (rows / records / documents) 

Ensure that **data** is **up-to-date *with* the rest**. 
(say, [[Denormalization|Denormalized]] field for some query).

Problems of **not having** em - <b><u>getting out of sync</u></b>:
1. inserting **related records** that're using **[[Foreign Key|Foreign Keys]]**;
2. when using **[[Denormalization]]** 
   (say, [[Composite Foreign Key|Denormalized foreign key]]), 
   the same data must be ***updated in* multiple places**;
3. **[[Secondary Index|Secondary Indexes]]** must be **kept up-to-date with main data**. If record's written w/o [[Database Index|Index]] update, query using that [[Database Index|Index]] will not read it.
