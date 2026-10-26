"""exm-product-of-inequalities (Section 2.4): bd - ac = b(d - c) + (b - a)c; the rule
0 <= a < b, 0 <= c < d => ac < bd; the warning's counterexample (-3)(-3) = 9 > 1 = (-1)(-1);
and the Quick check (b + b) - (a + a) = (b - a) + (b - a)."""
import itertools
from fractions import Fraction

QUOTED = {"warning": {"lhs": (-3, -3), "rhs": (-1, -1), "products": (9, 1)}}

G = range(-6, 7)
# the identity, on a grid of integers and on some rationals (a polynomial identity in four variables)
for a, b, c, d in itertools.product(G, repeat=4):
    assert b * d - a * c == b * (d - c) + (b - a) * c
for a, b, c, d in itertools.product([Fraction(1, 3), Fraction(-5, 7), Fraction(2), Fraction(0)], repeat=4):
    assert b * d - a * c == b * (d - c) + (b - a) * c
# the rule, in Z and in Q (both ordered commutative rings)
for a, b, c, d in itertools.product(range(0, 8), repeat=4):
    if a < b and c < d:
        assert a * c < b * d
        assert b > 0 and b * (d - c) > 0 and (b - a) * c >= 0
# the warning: the tempting rule fails
(a, c), (b, d) = QUOTED["warning"]["lhs"], QUOTED["warning"]["rhs"]
assert a < b and c < d
assert (a * c, b * d) == QUOTED["warning"]["products"] and a * c > b * d
# the Quick check
for a, b in itertools.product(G, repeat=2):
    assert (b + b) - (a + a) == (b - a) + (b - a)
    if a < b:
        assert a + a < b + b
print("exm-product-of-inequalities: all quoted values check")
