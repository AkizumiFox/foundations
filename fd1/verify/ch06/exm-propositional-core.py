"""exm-propositional-core (Section 6.3): the skeleton p -> (q or r), not q |= p -> r,
the B3 skeleton of the same section's core pattern, and the reading over Z on |n| <= 100:
P: n > 1, Q: n^2 = 2, R: n > 0. Both premises true, conclusion true."""
from _tt import entails, imp
assert entails("pqr", [lambda v: imp(v["p"], v["q"] or v["r"]), lambda v: not v["q"]],
               lambda v: imp(v["p"], v["r"]))
# the premises alone (p, q) do not give r: TAUT cannot act before instantiating
assert not entails("pqr", [lambda v: v["p"], lambda v: v["q"]], lambda v: v["r"])
W = range(-100, 101)
P = lambda n: n > 1
Q = lambda n: n * n == 2
R = lambda n: n > 0
assert all(imp(P(n), Q(n) or R(n)) for n in W)
assert all(not Q(n) for n in W)
assert all(imp(P(n), R(n)) for n in W)
print("exm-propositional-core: all quoted values check")
