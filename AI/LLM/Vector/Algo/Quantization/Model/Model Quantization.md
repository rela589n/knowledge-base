**Model [[Quantization]]** reduces model size and memory bandwidth
to ***fasten* [[Encoder|Encoding]] speed** and ***reduce* RAM usage**.

> This isn't directly related to whether we retrieve [[Vector Quantizaton|Quantized Vectors]] or not.

- Q8
- Q4

When training quantized model, there's a base "unquantized" which, not being quantized, performs worse than normal model since weights are adjusted to accord quantization.
