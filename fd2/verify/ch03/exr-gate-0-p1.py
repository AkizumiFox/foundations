"""Gate 0, P1: witnesses for property L (f(x) = x^2 fails it; 1_(0,inf) has it, not the swap)."""
from fractions import Fraction
Fr = Fraction

QUOTED = {
    "c_witness_x": 1,
    "c_y_range": (Fraction(1, 2), 1),    # \frac12 <= y < 1
    "c_bad_delta": 4, "c_bad_y": -1,     # y = 1 - delta/2 fails at delta = 4
    "d_swap": (4, 2),                    # x = d/4, y = -d/4, |y - x| = d/2
    "points": [2, 3, 2, 3],              # marking scheme (a)-(d)
}
assert sum(QUOTED["points"]) == 10

deltas = [Fr(1, 10**k) for k in range(8)] + [Fr(k, 7) for k in range(1, 60)] + [Fr(10**k) for k in range(6)]

# (c): y = 1 - min(delta, 1)/2
x = QUOTED["c_witness_x"]
for d in deltas:
    y = 1 - min(d, 1) / 2
    lo, hi = QUOTED["c_y_range"]
    assert lo <= y < hi
    assert abs(y - x) < d
    assert y * y < x * x
# the naive y = 1 - delta/2 fails at delta = 4
d = QUOTED["c_bad_delta"]
y = 1 - Fr(d, 2)
assert y == QUOTED["c_bad_y"] and not (y * y < 1)

# (d): f = indicator of (0, inf)
f = lambda t: 1 if t > 0 else 0
# property L: x > 0 with delta = x; x <= 0 with delta = 1; test sample y's
xs = [Fr(k, 9) for k in range(-40, 41)]
for x0 in xs:
    d = x0 if x0 > 0 else Fr(1)
    for k in range(-200, 201):
        y = x0 + d * Fr(k, 201)  # |y - x0| < d
        assert abs(y - x0) < d and f(y) >= f(x0)
# swap refuted: x = d/4, y = -d/4
q, h = QUOTED["d_swap"]
a, b, c = Fr(1, q), Fr(-1, q), Fr(1, h)
for d in deltas:
    x0, y = a * d, b * d
    assert abs(y - x0) == c * d < d and f(y) < f(x0)
print("ok")
