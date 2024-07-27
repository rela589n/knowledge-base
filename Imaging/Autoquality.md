---
aliases:
  - Compress image to desired size
tags:
  - feature
---
Reduces image size to the desired.

You configure:
- desired image size
- minimal allowed quality
- maximal allowed quality

This feature saves image multiple times comparing the different produced images to the desired image size. Most likely it uses [[Binary Search]] between min and max allowed quality parameters.
