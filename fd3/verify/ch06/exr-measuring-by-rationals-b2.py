"""exr-measuring-by-rationals-b2 (cube roots):
(1) y > 1 + a gives y^3 > y > a; m = min(1, a/2): 0 < m <= 1, m^3 <= m <= a/2 < a.
(2) z^3 - y^3 = (z - y)(z^2 + zy + y^2); z^2 + zy + y^2 = (z + y/2)^2 + (3/4) y^2.
(3) s^3 < a, h = min(1, (a - s^3)/(2(3s^2 + 3s + 1))): (s + h)^3 <= s^3 + h(3s^2 + 3s + 1) <= s^3 + (a - s^3)/2 < a.
(4) s^3 > a, h = (s^3 - a)/(3 s^2): 0 < h < s and (s - h)^3 - a = h^2 (3s - h) > 0; 3s - h > 2s."""
from fractions import Fraction as Fr
import random

QUOTED = {"h_low": "(a - s^3)/(2(3s^2 + 3s + 1))", "h_high": "(s^3 - a)/(3s^2)",
          "identity": "h^2(3s - h)", "m": r"\min\{1, a/2\}"}
random.seed(5)
for _ in range(2000):
    S, A, Y, Z, Hh = (Fr(random.randint(-999, 999), random.randint(1, 99)) for _ in range(5))
    assert (Z - Y) * (Z**2 + Z * Y + Y**2) == Z**3 - Y**3
    assert (Z + Y / 2) ** 2 + Fr(3, 4) * Y**2 == Z**2 + Z * Y + Y**2
    assert (S + Hh) ** 3 == S**3 + 3 * S**2 * Hh + 3 * S * Hh**2 + Hh**3
    if S != 0:
        H = (S**3 - A) / (3 * S**2)
        assert (S - H) ** 3 - A == H**2 * (3 * S - H)

def rq(lo, hi):
    return Fr(random.randint(int(lo * 1000), int(hi * 1000)), 1000)

for _ in range(5000):
    a = rq(0.001, 30)
    yy = 1 + a + rq(0.001, 5)
    assert yy ** 3 > yy > a
    m = min(Fr(1), a / 2)
    assert 0 < m <= 1 and m ** 3 <= m <= a / 2 < a
    ss = rq(0, 6)
    if ss ** 3 < a:
        hh = min(Fr(1), (a - ss ** 3) / (2 * (3 * ss ** 2 + 3 * ss + 1)))
        assert 0 < hh <= 1
        assert (ss + hh) ** 3 <= ss ** 3 + hh * (3 * ss ** 2 + 3 * ss + 1) <= ss ** 3 + (a - ss ** 3) / 2 < a
    elif ss ** 3 > a:
        assert ss > 0
        hh = (ss ** 3 - a) / (3 * ss ** 2)
        assert 0 < hh < ss and 3 * ss - hh > 2 * ss
        assert (ss - hh) ** 3 - a == hh ** 2 * (3 * ss - hh) > 0
    # strict increase of cubes
    y1, z1 = rq(-5, 5), rq(-5, 5)
    assert (y1 < z1) == (y1 ** 3 < z1 ** 3)
print("ok")
