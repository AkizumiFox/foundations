"""exm-four-tasks-with-quantifiers (Section 6.3): skeletons of (b), (c), the inconsistency
Quick check; the converse reading of (d) over Z; the wrong-subgoal Quick check's reading."""
from fractions import Fraction as F
from _tt import entails, satisfiable, imp
assert entails("pq", [lambda v: imp(v["p"], not v["q"])], lambda v: imp(v["q"], not v["p"]))
assert entails("pq", [lambda v: imp(v["q"], not v["p"])], lambda v: imp(v["p"], not v["q"]))
assert not satisfiable("pq", [lambda v: v["p"] and not v["q"], lambda v: imp(v["p"], v["q"])])
assert not satisfiable("p", [lambda v: v["p"] and not v["p"]])
# (d) converse: P even, Q positive over Z (window)
W = range(-50, 51)
even = lambda n: n % 2 == 0
pos = lambda n: n > 0
allP = all(even(n) for n in W)
assert not allP                              # so the premise forall P -> forall Q is true
assert imp(allP, all(pos(n) for n in W))
assert not all(imp(even(n), pos(n)) for n in W) and even(0) and not pos(0)
# wrong subgoal: eps0 = 1, a_n = L except a_{n0} = L + 0.75, N0 = n0
L, n0, eps0 = F(3), 5, F(1)
a = lambda n: L + F(3, 4) if n == n0 else L
N0 = n0
assert all(abs(a(n) - L) < eps0 for n in range(0, 200))          # instance at eps0, box line
assert all(abs(a(n) - L) < F(1, 10**6) for n in range(n0 + 1, 400))  # eventually constant
assert n0 >= N0 and abs(a(n0) - L) == F(3, 4) < 1
assert abs(2 * a(n0) - 2 * L) == F(3, 2) >= eps0
print("exm-four-tasks-with-quantifiers: all quoted values check")
