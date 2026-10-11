"""exr-cauchy-sequences-b1: (k+1)/(k+2) = 1 - 1/(k+2); (-1)^N - (-1)^(N+1) has absolute value 2."""
from fractions import Fraction as F
QUOTED = {"eps_b": 1, "gap_b": 2}
for k in range(500):
    assert F(k + 1, k + 2) == 1 - F(1, k + 2)
for N in range(50):
    assert abs((-1) ** N - (-1) ** (N + 1)) == 2
assert abs(1 - (-1)) == QUOTED["gap_b"] >= QUOTED["eps_b"]
print("ok")
