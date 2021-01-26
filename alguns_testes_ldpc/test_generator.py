from ldpc import generate_code

k = 256
m = 8
v = 32

P = generate_code(k, m, v)

# Test number of parity bits
assert len(P) == m*k/v

# Test number of elements per parity bit
for p in P:
  assert len(p) == v

# Test number of occurrences of {0,k-1} in P
for i in range(k):
  count = 0
  for p in P:
    if i in p:
      count += 1
  assert count == m
