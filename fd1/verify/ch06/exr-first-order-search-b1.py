"""exr-first-order-search-b1 (Section 6.3): the five breaking readings over Z and the TAUT
skeletons of claims 1, 6, 7, 11."""
from _tt import entails, satisfiable, imp
W = range(-50, 51)
# 2: R(x, y): x*y = 1. premise true (1*1 = 1); conclusion fails at x = 0
assert 1 * 1 == 1
assert not any(0 * y == 1 for y in range(-1000, 1001))
# 5: f(x) = x + 1, R is <
assert all(x < x + 1 for x in W) and not any(x + 1 < x for x in W)
# 8: P even, Q odd
assert all(x % 2 == 0 or x % 2 == 1 for x in W)
assert not all(x % 2 == 0 for x in W) and not (0 % 2 == 1)
# 10: P(x): x = 0, Q(x): x*x = x
assert all(imp(x == 0, x * x == x) for x in W)
assert any(x == 0 for x in W) and not (2 * 2 == 2)
# 12: R is <: every x has a larger y; < asymmetric (window [-50, 50])
assert all(any(x < y for y in range(x, x + 2)) for x in W)
assert all(imp(x < y, not (y < x)) for x in W for y in W)
# skeletons
assert entails("pqr", [lambda v: v["p"] and v["q"], lambda v: imp(v["p"], imp(v["q"], v["r"]))],
               lambda v: v["r"])                                              # claim 1
assert entails("pqr", [lambda v: imp(v["p"], v["q"]), lambda v: imp(v["q"], v["r"])],
               lambda v: imp(not v["r"], not v["p"]))                         # claim 6
assert entails("pq", [lambda v: v["p"] or v["q"], lambda v: not v["p"]], lambda v: v["q"])  # 7
assert not satisfiable("pq", [lambda v: v["p"] == (not v["q"]), lambda v: v["p"],
                              lambda v: v["q"]])                              # claim 11
# B3: p -> q, q -> not p |= not p; (b) p -> q |= not q -> not p
assert entails("pq", [lambda v: imp(v["p"], v["q"]), lambda v: imp(v["q"], not v["p"])],
               lambda v: not v["p"])
assert entails("pq", [lambda v: imp(v["p"], v["q"])], lambda v: imp(not v["q"], not v["p"]))
print("exr-first-order-search-b1: all quoted values check")
