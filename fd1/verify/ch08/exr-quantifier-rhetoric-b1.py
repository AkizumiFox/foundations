"""exr-quantifier-rhetoric-b1 (Ch 5, Section 5.2): (a) x = M + 1 refutes M; (b) x = -y, 1 - y;
(c) x = 1/delta, y = 1/delta + delta/2 give |x - y| < delta, |x^2 - y^2| = 1 + delta^2/4 >= 1."""
from fractions import Fraction as Fr

QUOTED = {"c_value": "1 + delta^2/4"}

for M in [Fr(-3), Fr(0), Fr(100)]:
    assert M + 1 > M
for y in [Fr(-2), Fr(0), Fr(5, 3)]:
    assert (-y) + y == 0 and (1 - y) + y == 1
for dv in [Fr(1), Fr(1, 10), Fr(3), Fr(2, 7), Fr(1, 1000), Fr(50)]:
    xv, yv = 1 / dv, 1 / dv + dv / 2
    assert abs(xv - yv) < dv and abs(xv**2 - yv**2) == 1 + dv**2 / 4 >= 1
# the trivial reading: delta = |x - y| makes |x - y| < delta false when x != y
for xv, yv in [(Fr(0), Fr(1)), (Fr(2), Fr(-3))]:
    assert not (abs(xv - yv) < abs(xv - yv))
print("exr-quantifier-rhetoric-b1: all quoted values check")
