"""exm-fraction-map-factorization: (1, 2) ~ (2, 4) since 1*4 = 2*2; the class of (1, 2)
begins (1, 2), (2, 4), (3, 6); numerators 1 != 2; f(a, b) = a/b agrees with ad = bc."""
from fractions import Fraction

QUOTED = {"pair": ((1, 2), (2, 4)), "class_start": [(1, 2), (2, 4), (3, 6)], "num": (1, 2)}
(a, b), (c, d) = QUOTED["pair"]
assert a * d == b * c == 4 and Fraction(a, b) == Fraction(c, d)
assert (a, c) == QUOTED["num"] and a != c
cls = sorted(((p, q) for q in range(1, 7) for p in range(-6, 7) if Fraction(p, q) == Fraction(1, 2)), key=lambda t: t[1])
assert cls == QUOTED["class_start"]
R = [(p, q) for p in range(-8, 9) for q in range(1, 9)]
assert all((Fraction(p, q) == Fraction(r, s)) == (p * s == q * r) for p, q in R for r, s in R)
print("exm-fraction-map-factorization: all quoted values check")
