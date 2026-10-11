"""exr-naturals-and-archimedes-c1: s_k = r + (s - r)/(k + 1) lies strictly between r and s and decreases in k;
(b) q = m/n with m the integer part of n x."""
from fractions import Fraction as Fr
import math

QUOTED = {}
r, s = Fr(1, 3), Fr(1, 2)
seq = [r + (s - r) / (k + 1) for k in range(1, 200)]
assert all(r < v < s for v in seq) and all(seq[i + 1] < seq[i] for i in range(len(seq) - 1))
for x in [Fr(-7, 3), Fr(0), Fr(5, 11), Fr(22, 7)]:
    for n in range(1, 30):
        m = math.floor(n * x)
        q = Fr(m, n)
        assert q <= x < q + Fr(1, n)
print("ok")
