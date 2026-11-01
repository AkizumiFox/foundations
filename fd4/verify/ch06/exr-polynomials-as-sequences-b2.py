"""exr-polynomials-as-sequences-b2 (Section 4.1): which sequences N -> Z/4Z are polynomials."""
QUOTED = {
    "a_first": [1, 2, 4, 8],   # 2^k for k = 0..3, classes [1], [2], [0], [0]
    "a_least_N": 1,
    "c_least_N": 0,
}
K = 400
a = [pow(2, k) % 4 for k in range(K)]
assert [pow(2, k) for k in range(4)] == QUOTED["a_first"]
assert a[0] == 1 and a[1] == 2 and all(v == 0 for v in a[2:])
assert max(k for k in range(K) if a[k]) == QUOTED["a_least_N"]
b = [(k * k) % 4 for k in range(K)]
assert all(b[k] == 1 for k in range(1, K, 2))          # never eventually zero
c = [(k * (k - 1) * (k - 2) * (k - 3)) % 4 for k in range(K)]
assert all(v == 0 for v in c)                          # zero polynomial, least N = 0
assert QUOTED["c_least_N"] == 0
d = [(2 * k) % 4 for k in range(K)]
assert all(d[k] == 2 for k in range(1, K, 2))
# the identities used in the solution
for j in range(200):
    assert (2 * j + 1) ** 2 == 4 * (j * j + j) + 1 and 2 * (2 * j + 1) == 4 * j + 2
for k in range(K):
    q, r = divmod(k, 4)
    assert k - r == 4 * q and (k - r) in (k, k - 1, k - 2, k - 3)
print("exr-polynomials-as-sequences-b2: ok")
