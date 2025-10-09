**Data warehouse** - [[OLAP]]-dedicated **read-only database**, 
which contains the **transformed copy** of [[OLTP]] database data in an **analysis-friendly** form.

*ETL (extract-transform-load)* - process of getting data to *Data Warehouse*.

The main benefit of having separate OLAP database is that it can be optimized for analytic access paterns (processing of large amount of data).