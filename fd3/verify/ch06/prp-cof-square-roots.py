"""prp-cof-square-roots: the constants of the existence proof, checked on many rationals.
(1) a + 1 bounds S: y > a + 1 > 0 gives y^2 > y > a.
(2) case s^2 < a: h = min(1, (a - s^2)/(2(2s + 1))) > 0 and
    (s + h)^2 <= s^2 + h(2s + 1) <= s^2 + (a - s^2)/2 < a  (s >= 0).
(3) case s^2 > a: h = (s^2 - a)/(2s) > 0, s - h = (s^2 + a)/(2s) > 0, (s - h)^2 = a + h^2 > a.
(4) uniqueness: (b - c)(b + c) = b^2 - c^2.
"""
from fractions import Fraction as Fr
import random

QUOTED = {"bound": "a + 1", "h_low": "(a - s^2)/(2(2s + 1))", "h_high": "(s^2 - a)/(2s)",
          "s_minus_h": "(s^2 + a)/(2s)", "square": "a + h^2"}

random.seed(6)
# polynomial / rational identities, checked at many rational points (exact arithmetic)
for _ in range(2000):
    S, A, Hh, B, C = (Fr(random.randint(-999, 999), random.randint(1, 99)) for _ in range(5))
    assert (S + Hh) ** 2 == S**2 + 2 * S * Hh + Hh**2
    assert (B - C) * (B + C) == B**2 - C**2
    if S != 0:
        H = (S**2 - A) / (2 * S)
        assert S - H == (S**2 + A) / (2 * S)
        assert (S - H) ** 2 == A + H**2

def rq(lo, hi):
    return Fr(random.randint(int(lo * 1000), int(hi * 1000)), 1000)

for _ in range(5000):
    a = rq(0.001, 50)
    # (1)
    y = a + 1 + rq(0.001, 10)
    assert y > 1 and y * y > y > a
    s = rq(0, 10)
    if s * s < a:
        h = min(Fr(1), (a - s * s) / (2 * (2 * s + 1)))
        assert h > 0 and h <= 1 and h * h <= h
        assert (s + h) ** 2 <= s * s + h * (2 * s + 1) <= s * s + (a - s * s) / 2 < a
    elif s * s > a:
        assert s > 0
        h = (s * s - a) / (2 * s)
        assert h > 0 and s - h == (s * s + a) / (2 * s) and s - h > 0
        assert (s - h) ** 2 == a + h * h and (s - h) ** 2 > a
print("ok")
