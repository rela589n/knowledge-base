---
tags:
  - solution
  - go
---
See https://github.com/cshum/imagor

In most features it is Go replacement of [[Thumbor]] (it uses the same url format).

Provides:
- [[Signed image urls]]
- [[Images with expiration time]]
- [[Resizing]]
- [[Basic Compression]] for jpeg
- [[MozJPEG optimizer]]
- [[Built-in image caching]] ([Result Storage](https://github.com/cshum/imagor?tab=readme-ov-file#loader-storage-and-result-storage))

Has [[Docker Image]]: [shumc/imagor](https://hub.docker.com/r/shumc/imagor/) with all necessary configuration options (easier to install compared to [[Thumbor]].
