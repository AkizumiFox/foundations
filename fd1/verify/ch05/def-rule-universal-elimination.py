"""def-rule-universal-elimination (Section 5.3): the algebra of "How this rule looks"
and the readings in "Common errors", with the three worlds of Figure C3. Polynomial identities of degree <= 2 are checked at
many exact rational points (agreement at 3 points already forces identity)."""
from fractions import Fraction as Fr
import sys
sys.path.insert(0, "verify/ch05")
from _fo_models import structure, sat, P, ALL, EX, NOT, OR, IMP

QUOTED = {
    "(a-1)^2 expanded": "a^2 - 2 \\cdot a + 1",
    "buried: c": 1,
    "partial replacement fails when x names": 1,
}
pts = [Fr(k, 13) for k in range(-200, 200)]

# "How this rule looks": (a - 1)^2 = a^2 - 2a + 1 (the arith premise's instance).
expanded = lambda a: a * a - 2 * a + 1          # the string QUOTED above, as a function
assert all((a - 1) ** 2 == expanded(a) for a in pts)

# Capture: over N, x + 1 != x, so exists y (y != x) holds for every x; y != y never holds.
assert all(n + 1 != n for n in range(1000))
assert not any(n != n for n in range(1000))

# Buried quantifier over N: forall x (x >= 1) is false (0 fails), so the line is true;
# with c = 1: P(1) is 1 >= 1 (true), Q(1) is 1 = 0 (false), so P(c) -> Q(c) is false.
assert not all(n >= 1 for n in range(0, 1000)) and not (0 >= 1)
c = QUOTED["buried: c"]
assert (c >= 1) and not (c == 0)

# Partial replacement: forall x (x <= x^2 or x < 1) on R; for x >= 1, x^2 - x = x(x - 1) >= 0.
for t in pts:
    assert t <= t * t or t < 1
    if t >= 1:
        assert t * t - t == t * (t - 1) >= 0
t = QUOTED["partial replacement fails when x names"]
assert not (2 <= t * t or t < 1)       # 2 <= 1 or 1 < 1 is false
# Figure C3: three tiny worlds; in each the premise is true and the faulty line false.
NE = lambda s, t: NOT(("eq", s, t))
cap = structure([0, 1])
assert sat(ALL("x", EX("y", NE("y", "x"))), cap, {})
assert not sat(EX("y", NE("y", "y")), cap, {})
c = ("c", "c")
bur = structure([0, 1], const={"c": 1}, pred={"P": {(1,)}, "Q": {(0,)}})
assert sat(IMP(ALL("x", P("P", "x")), P("Q", c)), bur, {})
assert not sat(IMP(P("P", c), P("Q", c)), bur, {})
some = structure(["a", "b"], const={"c": "a"}, pred={"P": {("b",)}})
assert sat(ALL("x", OR(P("P", "x"), NOT(P("P", "x")))), some, {})
assert not sat(OR(P("P", c), NOT(P("P", "x"))), some, {"x": "b"})
assert sat(OR(P("P", c), NOT(P("P", c))), some, {"x": "b"})
print("def-rule-universal-elimination: all quoted values check")
