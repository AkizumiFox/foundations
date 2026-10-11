"""The Quick check after exm-termwise-reciprocal-ill-defined: (1 + 1/(n+1)) * 2 - 2 = 2/(n+1)."""
from fractions import Fraction as F

QUOTED = {"representative": "2/(n+1)"}
for n in range(500):
    assert (1 + F(1, n + 1)) * 2 - 2 == F(2, n + 1)
print("ok")
