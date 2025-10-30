Variable length integers instead of using all 8 bytes of data, reduce this number via additional bit per each next byte of data - it indicates if there are any more bytes to come. For instance, 1337 is encoded as `1|111001|0|0|0010100` instead of `<a_lot_of_zeros>001000|1110001`. Bit right after first byte is used to indicate sign of number.

Hence integers between:
- -64 and 63 are encoded with one byte;
- -8192 and 8191 are encoded with two bytes;
- and so on...