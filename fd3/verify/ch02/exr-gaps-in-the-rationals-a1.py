"""exr-gaps-in-the-rationals-a1 (b): t(3/2) = 17/12 < 3/2 (34 < 36); u(7/5) = 140/99 in A,
140/99 > 7/5 (700 > 693), 140^2 = 19600 < 19602 = 2*99^2; 49 < 50, 9 > 8.
(c): in a field with r^2 = 2, t(r) = u(r) = r: checked as rational-function identities
t(s) - s = (2 - s^2)/(2s), u(s) - s = s(2 - s^2)/(s^2 + 2), both vanishing when s^2 = 2."""
from fractions import Fraction as F
QUOTED = {"t32": F(17, 12), "u75": F(140, 99), "sq": (19600, 19602), "cross": (700, 693, 34, 36)}
t = lambda s: (s*s + 2) / (2*s)
u = lambda s: 4*s / (s*s + 2)
assert t(F(3, 2)) == QUOTED["t32"] and t(F(3, 2)) < F(3, 2) and F(17, 12)**2 > 2
assert u(F(7, 5)) == QUOTED["u75"] and F(28, 5) / F(99, 25) == F(140, 99)
assert (140**2, 2*99**2) == QUOTED["sq"] and F(140, 99)**2 < 2
assert (140*5, 7*99, 17*2, 3*12) == QUOTED["cross"]
assert F(140, 99) > F(7, 5) and F(49, 25) < 2 and F(9, 4) > 2
for s in [F(a, b) for a in range(1, 30) for b in range(1, 20)]:
    assert t(s) - s == (2 - s*s) / (2*s) and u(s) - s == s*(2 - s*s) / (s*s + 2)
print("ok")
