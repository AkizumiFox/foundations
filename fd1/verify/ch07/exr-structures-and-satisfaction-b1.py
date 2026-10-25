"""exr-structures-and-satisfaction-b1 (Section 7.1): the four sentences in the divisors of 12 under
divisibility and in the chain 1..6; the Hasse edges are the covering pairs; only (iii) separates."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, P, ALL, EX, AND, OR

D1 = [1, 2, 3, 4, 6, 12]
div = {(x, y) for x in D1 for y in D1 if y % x == 0}
cover = {(x, y) for (x, y) in div if x != y
         and not any(z not in (x, y) and (x, z) in div and (z, y) in div for z in D1)}
assert cover == {(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)}
D2 = [1, 2, 3, 4, 5, 6]
M1 = structure(D1, pred={"<=": div})
M2 = structure(D2, pred={"<=": {(x, y) for x in D2 for y in D2 if x <= y}})
le = lambda a, b: P("<=", a, b)
S = {"i": EX("x", ALL("y", le("x", "y"))),
     "ii": EX("x", ALL("y", le("y", "x"))),
     "iii": ALL("x", ALL("y", OR(le("x", "y"), le("y", "x")))),
     "iv": ALL("x", ALL("y", EX("z", AND(le("x", "z"), le("y", "z")))))}
QUOTED = {"i": (True, True), "ii": (True, True), "iii": (False, True), "iv": (True, True)}
for k, f in S.items():
    assert (sat(f, M1, {}), sat(f, M2, {})) == QUOTED[k]
# witnesses
assert sat(ALL("y", le("x", "y")), M1, {"x": 1}) and sat(ALL("y", le("x", "y")), M2, {"x": 1})
assert sat(ALL("y", le("y", "x")), M1, {"x": 12}) and sat(ALL("y", le("y", "x")), M2, {"x": 6})
assert not sat(OR(le("x", "y"), le("y", "x")), M1, {"x": 2, "y": 3})
for x in D1:
    for y in D1:
        assert (x, 12) in div and (y, 12) in div
for x in D2:
    for y in D2:
        assert max(x, y) >= x and max(x, y) >= y and 6 >= x and 6 >= y
assert [k for k in S if QUOTED[k][0] != QUOTED[k][1]] == ["iii"]
print("exr-structures-and-satisfaction-b1: all quoted values check")
