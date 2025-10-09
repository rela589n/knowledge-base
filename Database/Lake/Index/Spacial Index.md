---
aliases:
  - Multi-dimensional Index
---
For spatial data, R-Tree indexes may be used (PostGIS uses them). Not so commonly, for 2D coordinates range filter (all points within rectangle), the longitude + latitude may be translated into single value using space filling curve.

> Multi-dimensional indexes may be used not only for geographic data. They may be used for any kind of multi-dimensional range queries - like colors range (red, green, blue), date + temperature range and so on.

