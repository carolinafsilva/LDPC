# Trabalho 2 - Codigo LDPC
# Teoria da Informacao
# 2020/21

# Ana Carolina Ferreira da Silva
# up202004100

from bitstring import BitArray
from numpy.random import shuffle


def generate_code(k: int, m: int, v: int):
  '''
  Generates a list P with m(k/v) lists of size v
  '''
  P = []
  I = [i for i in range(k)]
  for _ in range(m):
    shuffle(I)
    for j in range(k//v):
      start = j * v
      end = j * v + v
      P.append(I[start : end])
  return P


def encode(_: int, P: list, w: BitArray):
  '''
  Encondes a message w of size k with a block code defined by a list P
  '''
  x = BitArray(w)
  for p in P:
    xor = False
    for i in p:
      xor ^= w[i]
    x.append(bin(xor))
  return x


def _check_error(q: BitArray):
  '''
  Returns True if q has at least one bit as 1, False otherwise
  '''
  return q.uint > 0


def _fix_bit(i: int, K: int, P: list, y: BitArray, q: BitArray):
  '''
  Tries to fix an error in y at index i.

  Return fixed bit or None if no fix is possible.
  '''
  N = len(P)
  for j in range(N):
    if not q[K+j] and i in P[j]:
      xor = y[K+j]
      for b in P[j]:
        if b == i:
          continue
        elif q[b] == 0:
          xor ^= y[b]
        else:
          break
      else:
        return xor
  return None


def decode(K: int, P: list, y: BitArray, q: BitArray):
  '''
  Tries to decode y.

  Returns decoding of y or None if decoding is not possible
  '''
  last_q = BitArray()
  while _check_error(q[:K]) and last_q != q:
    last_q = BitArray(q)
    for i in range(K):
      if q[i]:
        r = _fix_bit(i, K, P, y, q)
        if r != None:
          y[i] = bin(r)
          q[i] = 0

  if _check_error(q[:K]):
    return None
  return y
