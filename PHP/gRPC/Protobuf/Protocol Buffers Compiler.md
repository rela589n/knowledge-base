---
aliases:
  - protoc
---
Protocol Buffers Compiler compiles  `.proto` files into language-specific formats.

Protoc itself is a **generic tool**. To run compilation into your needed format you'd need to install appropriate plugin.

For example, in order to convert `message.proto` file into java class, you'd need java [[Protoc plugin|Plugin]]. To convert into php - you'd need php [[Protoc plugin|Plugin]].

It can be installed with this guide: https://protobuf.dev/installation/

