In **BinaryProtocol** object field values are encoded in following way: 
- Field type - 1 byte;
- [[Field tag]] - 2 bytes. 
- Rest data varies depending on the field type. 

For _string_: length of data - 4 bytes followed by actual data. 

For _integer_: 8 bytes which make up number.

For _list_: item type (_string_ in example) - 1 byte, number of items - 4 bytes. Rest is the actual data (string lengths respectively followed by strings itself).

The last byte is null-terminator. It is necessary to separate parts of the data that belong together.
