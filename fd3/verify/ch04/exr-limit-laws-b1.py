"""exr-limit-laws-b1: rewritings through u = 1/(n+1) and the limits 1/3, 1, -6."""
from fractions import Fraction as Q

QUOTED = {"a": Q(1, 3), "b": 1, "c": -6}
for k in range(5000):
    u = Q(1, k + 1)
    assert Q(k + 2, 3 * k + 1) == (1 + u) / (3 - 2 * u)
    assert 0 < u <= 1 and 3 - 2 * u >= 1
    assert Q(k * k + 1, (k + 1) ** 2) == 1 - 2 * u + 2 * u * u
    # the three sequences approach their limits at rate O(u)
    assert abs((1 + u) / (3 - 2 * u) - QUOTED["a"]) <= 2 * u
    assert abs((1 - 2 * u + 2 * u * u) - QUOTED["b"]) <= 4 * u
    assert abs((u - 2) * (3 + (-1) ** k * u) - QUOTED["c"]) <= 6 * u
assert (0 - 2) * (3 + 0) == QUOTED["c"]
print("ok")
