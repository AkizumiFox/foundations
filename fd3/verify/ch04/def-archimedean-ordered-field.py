"""def-archimedean-ordered-field: the Quick check (n > 355/113; least n with 1/n < 7/500)."""
from fractions import Fraction as Fr

QUOTED = {"n_above": 4, "products_113": (339, 452), "least_n": 72, "products_7": (497, 504)}
assert (113 * 3, 113 * 4) == QUOTED["products_113"]
assert min(n for n in range(1, 100) if Fr(355, 113) < n) == QUOTED["n_above"]
assert (7 * 71, 7 * 72) == QUOTED["products_7"]
assert min(n for n in range(1, 1000) if Fr(1, n) < Fr(7, 500)) == QUOTED["least_n"]
assert all(Fr(1, n) < Fr(7, 500) for n in range(72, 2000))
print("ok")
