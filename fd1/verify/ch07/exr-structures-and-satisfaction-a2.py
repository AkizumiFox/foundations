"""exr-structures-and-satisfaction-a2 (Section 7.1): the twelve drill answers."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, P, ALL, EX, NOT, AND, OR, IMP

# (a), (b): D = {a, b}, P = {a}
M = structure("ab", pred={"P": {("a",)}})
assert not sat(ALL("x", P("P", "x")), M, {}) and not sat(P("P", "x"), M, {"x": "b"})
assert sat(EX("x", NOT(P("P", "x"))), M, {}) and sat(NOT(P("P", "x")), M, {"x": "b"})
# (c) x*x + 1 at x = -2
assert (-2) * (-2) + 1 == 5
# (d) free variables x, z; z never matters; x matters in (N, <=) but not when <= is empty
D = [0, 1, 2]
Mo = structure(D, pred={"<=": {(a, b) for a in D for b in D if a <= b}})
f = AND(ALL("y", P("<=", "x", "y")), ("eq", "z", "z"))
for x in D:
    vals = {sat(f, Mo, {"x": x, "z": z, "y": 0}) for z in D}
    assert len(vals) == 1
assert {sat(f, Mo, {"x": x, "z": 0}) for x in D} == {True, False}  # x does matter
assert sat(f, Mo, {"x": 0, "z": 0}) and not sat(f, Mo, {"x": 1, "z": 0})  # l(x) = 0 vs 1
Me = structure(D, pred={"<=": set()})
assert {sat(f, Me, {"x": x, "z": z}) for x in D for z in D} == {False}  # <= empty: x does not matter
# (e) exists x forall y (x <= y) in {0,1,2}, witness 0
assert sat(EX("x", ALL("y", P("<=", "x", "y"))), Mo, {})
assert sat(ALL("y", P("<=", "x", "y")), Mo, {"x": 0})
# (f) in N: l(x) = 3, witness y = 0; l(x) = 0, nothing below 0
assert 0 < 3 and not any(y < 0 for y in range(0, 1000))
# (g) Figure F left
FL = structure("abc", pred={"P": {("a",)}, "R": {("a", "b"), ("b", "b"), ("c", "a")}})
assert sat(ALL("x", IMP(P("P", "x"), EX("y", P("R", "y", "x")))), FL, {})
assert FL["pred"]["P"] == {("a",)} and ("c", "a") in FL["pred"]["R"]
# (h) comparability: true in N (total order); false in divisibility on {1,2,3,6} at 2, 3
DR = [1, 2, 3, 6]
Md = structure(DR, pred={"<=": {(x, y) for x in DR for y in DR if y % x == 0}})
comp = ALL("x", ALL("y", OR(P("<=", "x", "y"), P("<=", "y", "x"))))
assert not sat(comp, Md, {})
assert not sat(OR(P("<=", "x", "y"), P("<=", "y", "x")), Md, {"x": 2, "y": 3})
# (i) exists x forall y (y*x = y): Z with x = 1; even integers: y = 2 forces x = 1, odd
assert all(y * 1 == y for y in range(-100, 101))
assert [x for x in range(-100, 101) if 2 * x == 2] == [1] and 1 % 2 == 1
# (j) 0 - 1 not in N
assert 0 - 1 < 0
# (k) D = {a}, P empty: both sentences true
M1 = structure("a", pred={"P": set()})
s1 = IMP(ALL("x", P("P", "x")), EX("x", P("P", "x")))
s2 = IMP(ALL("x", NOT(P("P", "x"))), NOT(EX("x", P("P", "x"))))
assert sat(s1, M1, {}) and not sat(ALL("x", P("P", "x")), M1, {})
assert sat(s2, M1, {}) and sat(ALL("x", NOT(P("P", "x"))), M1, {}) and sat(NOT(EX("x", P("P", "x"))), M1, {})
# (l) {1, 2}, R = {(1,2), (2,1)}
Ml = structure([1, 2], pred={"R": {(1, 2), (2, 1)}})
assert not sat(EX("x", P("R", "x", "x")), Ml, {}) and sat(ALL("x", EX("y", P("R", "x", "y"))), Ml, {})
print("exr-structures-and-satisfaction-a2: all quoted values check")
