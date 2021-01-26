
from bitstring import BitArray

from ldpc import decode, encode

K = 8
N = 16
P = [[0,2],[1,3],[0,1],[2,3],[4,6],[5,7],[4,5],[6,7]]
w = BitArray('0b10110011')
x = encode(K, P, w)
assert x == BitArray('0b1011001101101100')
y = BitArray('0b0001000101101100')
q = BitArray('0b1110101000000010')
hat_y = decode(K, P, y, q)
assert hat_y is not None
hat_w = hat_y[:K]
assert hat_w == w
