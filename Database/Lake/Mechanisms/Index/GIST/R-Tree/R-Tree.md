**R-Tree** (Rectangle [[Balanced Tree|Tree]]) - [[GIST Index]] that organizes plane into rectangles / ranges that cover it.

Useful both for:
- spatial information;
- ranges (like time).

Points on plane:
![[R-Tree.png]]

[[GIST Index]] for these [[Point]]s:

![[GiST R-Tree Index.png]]

Search all points in the rectangle:
```sql
select *
from points
where p <@ box '(2,1),(7,4)';
```

![[Search points in Rectangle.png]]

That's how it's searched:
![[Search in R-Tree.png]]

Search includes rectangle if it intersects with query.
