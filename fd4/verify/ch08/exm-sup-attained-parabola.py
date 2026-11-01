"""exm-sup-attained-parabola and Quick check 3 (section 8.3)."""
from fractions import Fraction as Fr
import math

QUOTED = {"sup": Fr(1, 4), "argmax": Fr(1, 2), "inf": Fr(0), "qc3_sup": 4, "qc3_inf": 0}

g = lambda x: x * (1 - x)
for k in range(0, 101):
    x = Fr(k, 100)
    assert g(x) == Fr(1, 4) - (x - Fr(1, 2))**2      # completing the square
    assert 0 <= g(x) <= QUOTED["sup"]
assert g(QUOTED["argmax"]) == QUOTED["sup"] and g(Fr(0)) == QUOTED["inf"] == g(Fr(1))

# Quick check 3: x^2 on (-1, 2) has values [0, 4)
vals = [Fr(k, 1000)**2 for k in range(-999, 2000)]
assert min(vals) == QUOTED["qc3_inf"] and max(vals) < QUOTED["qc3_sup"]
assert all((Fr(t, 100) <= 4) for t in range(0, 400))
# sqrt2/2 lies in [0, 1]
assert 0 <= math.sqrt(2) / 2 <= 1 and 2 <= 4
print("ok")
