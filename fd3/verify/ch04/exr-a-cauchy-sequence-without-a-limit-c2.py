"""exr-a-cauchy-sequence-without-a-limit-c2: 1/(N+1) - 1/(N+2) = 1/((N+1)(N+2)) > 0."""
from fractions import Fraction as F
QUOTED = {"m_minus": 0, "n_plus": 1}
for N in range(1000):
    assert F(1, N + 1) - F(1, N + 2) == F(1, (N + 1)*(N + 2)) > 0
assert QUOTED == {"m_minus": 0, "n_plus": 1}
print("ok")
