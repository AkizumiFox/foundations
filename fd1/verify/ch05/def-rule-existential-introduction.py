"""def-rule-existential-introduction (Ch 4, Section 4.5) and the prose of that section:
the table of readings of R(c, c), the capture nonexample, the Quick check on 2 + 2 = 4,
the hook, the bounded witness and the 'large enough' warning (N = 100), clause 3's recipe,
and the even/odd witnesses of 'How this rule looks in a mathematical proof'."""
from fractions import Fraction as Fr
from _s0102_fol import V, C, F, At, Eq, All, Ex, sub, free_for

QUOTED = {"hook N": 100, "even witness": 3, "odd witness": 3, "rows of the table": 4,
          "least bounded witness": 100}

x, y, c = V('x'), V('y'), C('c')
line = At('R', c, c)
# the table: four phi, each with phi[c/x] equal to the cited line R(c, c)
table = [At('R', x, c), At('R', c, x), At('R', x, x), At('R', c, c)]
assert len(table) == QUOTED["rows of the table"]
for phi in table:
    assert sub(phi, c, 'x') == line and free_for(c, 'x', phi)
# the readings over N with R as <= and c = 5 are true (witnesses 0, 5, 0)
N = range(0, 100)
assert any(d <= 5 for d in N) and any(5 <= d for d in N) and any(d <= d for d in N)

# clause 3: the recipe fails when x appears in the line: R(x, c), marking c, gives R(x, x)
bad = At('R', x, x)
assert sub(bad, c, 'x') == At('R', c, c) != At('R', x, c)

# capture: phi = forall y R(x, y), t = y: phi[y/x] is the cited line, y is not free for x
phi = All('y', At('R', x, y))
assert sub(phi, y, 'x') == All('y', At('R', y, y))
assert not free_for(y, 'x', phi)
# over Z (window), every integer is <= itself, and no integer is <= every integer
W = range(-60, 61)
assert all(d <= d for d in W)
assert all(any(not (d <= e) for e in range(d - 1, d + 1)) for d in W)   # e = d - 1 < d

# Quick check: line 2 + 2 = 4; three phi, witnesses 2, 2, 4
two, four = C('2'), C('4')
plus = lambda a, b: F('+', a, b)
L = Eq(plus(two, two), four)
for phi, t in [(Eq(plus(x, x), four), two), (Eq(plus(x, two), four), two),
               (Eq(plus(two, two), x), four)]:
    assert sub(phi, t, 'x') == L and free_for(t, 'x', phi)

# hook and bounded witness: 1/(N + 1) < 1/100 at N = 100, not at N = 99
assert Fr(1, 100 + 1) < Fr(1, 100)
assert not (Fr(1, 99 + 1) < Fr(1, 100))
least = min(n for n in range(0, 1000) if Fr(1, n + 1) < Fr(1, 100))
assert least == QUOTED["least bounded witness"] == QUOTED["hook N"]

# 6 = 2 * 3, 7 = 2 * 3 + 1; 2n + 1 is odd and exceeds 2n
assert 6 == 2 * QUOTED["even witness"] and 7 == 2 * QUOTED["odd witness"] + 1
assert all((2 * n + 1) % 2 == 1 and 2 * n + 1 > 2 * n for n in W)
print("def-rule-existential-introduction: all quoted values check")
