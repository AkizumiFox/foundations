"""exm-self-explanation (Section 5.4) and the strategies passage after it:
x + 1/x >= 2 for x > 0 (lines 1-4 and their algebra); the false variant at x = -1 gives -2;
equality at x = 1; sqrt(xy) <= (x + y)/2 via x + y - 2 sqrt(xy) = (sqrt x - sqrt y)^2,
the instance x = 1, y = 4 (both sides 1), the squaring route (x + y)^2 - 4xy = (x - y)^2,
and y = 1/x giving sqrt(xy) = 1; a^2 <= b^2 with b >= 0 gives a <= b, failing at a = 1, b = -2."""
import math
from fractions import Fraction as Fr

QUOTED = {"bad x": -1, "bad value": -2, "equality x": 1, "example x": 1, "example y": 4,
          "example both sides": 1, "refl a": 1, "refl b": -2}
pts = [Fr(a, b) for a in range(1, 40) for b in range(1, 9)]
for x in pts:
    assert (x - 1) ** 2 == x * x - 2 * x + 1 >= 0
    assert (x * x - 2 * x + 1) / x == x - 2 + 1 / x >= 0
    assert x + 1 / x >= 2
x = Fr(QUOTED["bad x"])
assert x + 1 / x == QUOTED["bad value"] < 2
assert (x * x - 2 * x + 1) >= 0 and (x * x - 2 * x + 1) / x < 0     # division by x < 0 flips
e = Fr(QUOTED["equality x"])
assert (e - 1) ** 2 == 0 and e + 1 / e == 2
# AM-GM for two numbers
xs, ys = QUOTED["example x"], QUOTED["example y"]
lhs = xs + ys - 2 * math.isqrt(xs * ys)
assert math.isqrt(xs * ys) ** 2 == xs * ys and lhs == (1 - 2) ** 2 == QUOTED["example both sides"]
for a in pts[:80]:
    for b in pts[:80:7]:
        assert (a + b) ** 2 - 4 * a * b == (a - b) ** 2
        assert a * b <= (a + b) ** 2 / 4
for a in [0.3, 1.0, 2.5, 7.0, 13.0]:
    for b in [0.2, 1.0, 4.0, 9.0]:
        assert abs((a + b - 2 * math.sqrt(a * b)) - (math.sqrt(a) - math.sqrt(b)) ** 2) < 1e-12
        assert math.sqrt(a * b) <= (a + b) / 2 + 1e-12
    assert abs(math.sqrt(a * (1 / a)) - 1) < 1e-12
# order reflection: a^2 <= b^2 and b >= 0 imply a <= b; fails without b >= 0
for a in range(-20, 21):
    for b in range(0, 21):
        if a * a <= b * b:
            assert abs(a) <= b and a <= b
ra, rb = QUOTED["refl a"], QUOTED["refl b"]
assert ra * ra <= rb * rb and not ra <= rb
print("exm-self-explanation: all quoted values check")
