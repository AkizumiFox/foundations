"""def-rule-universal-elimination (Ch 4, Section 4.3): the algebra of "How this rule looks"
and the readings in "Common errors". Polynomial identities of degree <= 2 are checked at
many exact rational points (agreement at 3 points already forces identity)."""
from fractions import Fraction as Fr

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
print("def-rule-universal-elimination: all quoted values check")
