First of all, it's necessary to install [[Protocol Buffers Compiler|protoc]] binary.

Then, to generate Client, we can use native [[grpc_php_plugin]], as it's supported by Google (note that it's only clients that are supported for PHP - servers aren't supported).

To generate Server, we can use [[protoc-gen-php-grpc]], provided by [[RoadRunner]]. Actually, it should support client as well.

