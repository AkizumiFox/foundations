"""exm-square-three-ways (Ch 6 Section 6.4): witnesses 1, -1 against injectivity, -1 against
surjectivity; injectivity on [0, oo) checked on a grid."""
from fractions import Fraction as F

QUOTED = {"witnesses": (1, -1)}

assert 1 ** 2 == (-1) ** 2 and 1 != -1
pts = [F(k, 6) for k in range(0, 61)]
assert len({x * x for x in pts}) == len(pts)
assert all(x * x >= 0 > -1 for x in [F(k, 6) for k in range(-60, 61)])
print("exm-square-three-ways: all quoted values check")
