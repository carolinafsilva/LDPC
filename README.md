# LDPC

## Dependencies
In order to use the module you need to install the following dependencies: *bitstring* and *numpy*.

## How to use the module

In the begining of your python code import the functions you intend to use, as follow
```py
from ldpc.py import encode, decode
```

### How to generate a block code?
Start by importing the *generate_code* function.

This function receives 3 inputs
- *k*: size of the message to code
- *m*: number of times each message bit is gonna be used
- *v*: number of bits needed to generate a parity bit

The function returns a list of size *m(k/v)* with lists of size *v*

Example:
```py
k = 9
m = 2
v = 2
P = generate_code(k, m, v)
```

### How to code a message?
Start by importing the *encode* function.

The function receives 3 inputs
- *k* : size of the message to code
- *P* : block code (see *generate_code* function)
- *w* : message to code

The function returns a *BitArray* with the message *w*, with the parity bits concatenated.

Example:
```py
k = 32
m = 8
v = 4
w = BitArray('0b01001000010001110111100010010101')
P = generate_code(k, m, v)
x = encode(k, P, w)
```

### How to decode a coded message?
Start by importing the *decode* function

The function needs 4 arguments:
- *k* : size of the message to code
- *P* : block code (see *generate_code* function)
- *y* : code received from the Binary Eraser Channel
- *q* : errors detected in *y*

The function returns a *BitArray* with the message *w* decoded or *None* if it's not possible to decode.

Example:
```py
k = 8
m = 2
v = 2
P = generate_code(k, m, v)
y = BitArray('0b0001000101101100')
q = BitArray('0b1110101000000010')
x = decode(k, P, y, q)
```
