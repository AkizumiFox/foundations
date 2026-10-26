"""exr-gaps-in-the-rationals-b4: (a) no x = p/q with x^2 = 8 (brute force over small p, q) and the
reduction (x/2)^2 = x^2/4; (b) the counterexample x = 1, y = -2; (c) (2/s)^2 < 2 for s > 0 with
s^2 > 2, over a grid of s; (d) s = 7/5: 49 < 50, s + 1/10 = 3/2, 9/4 > 2."""
from fractions import Fraction as F
QUOTED = {"b": (1, -2), "d_s": F(7, 5), "d_next": F(3, 2)}
# (a)
assert not any(p*p == 8*q*q for p in range(1, 3000) for q in range(1, 1100))
for x in [F(a, b) for a in range(-20, 21) for b in range(1, 10)]:
    assert (x / 2)**2 == x*x / 4
# (b)
x, y = QUOTED["b"]
assert x*x < y*y and x > y and (x*x, y*y) == (1, 4)
# (c)
for s in [F(a, b) for a in range(1, 80) for b in range(1, 30)]:
    if s*s > 2:
        assert (2 / s)**2 == 4 / (s*s) < 2
        assert 1 / (s*s) < F(1, 2)
# (d)
s = QUOTED["d_s"]
assert s*s == F(49, 25) < 2 and 49 < 50
assert s + F(1, 10) == QUOTED["d_next"] and QUOTED["d_next"]**2 == F(9, 4) > 2 and 9 > 8
print("ok")
