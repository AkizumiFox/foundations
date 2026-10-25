"""exr-finite-sets-c2: |A x B| = mn and |B^A| = n^m for small m, n, including 0 cases."""
from itertools import product
QUOTED = {"zero_pow_zero": 1}
assert 0**0 == QUOTED["zero_pow_zero"]
for m in range(0, 5):
    for n in range(0, 5):
        A = range(m); B = range(n)
        assert len(list(product(A, B))) == m * n
        funcs = list(product(B, repeat=m))   # a function A -> B is its tuple of values
        assert len(funcs) == n**m
        if m >= 1 and n == 0:
            assert len(funcs) == 0
print("ok")
