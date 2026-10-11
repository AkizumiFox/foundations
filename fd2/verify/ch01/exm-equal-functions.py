"""exm-equal-functions (Ch 6 Section 6.4): (x+1)^2 - 2x - 1 = x^2 and sqrt(x^2) = |x|,
checked on rational sample points (the first as a polynomial identity: degree 2, more
than three points)."""
from fractions import Fraction as F

QUOTED = {"identities checked": True}

pts = [F(k, 7) for k in range(-50, 51)]
assert all((x + 1) ** 2 - 2 * x - 1 == x * x for x in pts)
assert all(abs(x) >= 0 and abs(x) ** 2 == x * x for x in pts)
print("exm-equal-functions: all identities check")
