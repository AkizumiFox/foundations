"""exr-connective-rhetoric-b1 (Ch 5, Section 5.1): (sqrt a - sqrt b)^2 = a - 2 sqrt(ab) + b, AM >= GM."""
import math
from fractions import Fraction as Fr

QUOTED = {"expansion a - 2 sqrt(ab) + b checked below": True}

# exact on perfect squares a = p^2, b = q^2 (sqrt a = p, sqrt b = q, sqrt(ab) = pq)
for p in [Fr(1), Fr(2), Fr(1, 3), Fr(5, 2)]:
    for q in [Fr(1), Fr(3), Fr(2, 7)]:
        a, b = p * p, q * q
        assert (p - q)**2 == a - 2 * (p * q) + b >= 0
        assert (a + b) / 2 >= p * q
# numerically elsewhere
for a, b in [(2.0, 8.0), (1 / 3, 5.0), (7.0, 7.0), (0.01, 900.0)]:
    lhs = (math.sqrt(a) - math.sqrt(b))**2
    assert abs(lhs - (a - 2 * math.sqrt(a * b) + b)) < 1e-9 * (1 + a + b)
    assert (a + b) / 2 >= math.sqrt(a * b) - 1e-12
print("exr-connective-rhetoric-b1: all quoted values check")
