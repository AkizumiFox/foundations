"""exm-rhetoric-induction (Ch 5, Section 5.2): 0 < a^n <= 1 for 0 < a <= 1; a^n <= a fails at n = 0
for a < 1; |a - b| = max - min; the warning max{2, 1} = 2 != 1; the subsection after it:
forall y exists x (x^2 > y) with x = y + 1 (y >= 0), x = 0 (y < 0); exists x forall y fails at y = x^2."""
from fractions import Fraction as Fr

QUOTED = {"warning_pair": (2, 1), "warning_max": 2}

for a in [Fr(1), Fr(1, 2), Fr(9, 10), Fr(1, 1000)]:
    p = Fr(1)
    for n in range(0, 60):
        assert 0 < p <= 1          # P(n)
        nxt = p * a
        assert 0 < nxt and nxt <= p <= 1   # the step's two inequalities
        p = nxt
    if a < 1:
        assert not (a**0 <= a)     # a^n <= a fails at n = 0
for a in [Fr(k, 3) for k in range(-9, 10)]:
    for b in [Fr(k, 4) for k in range(-8, 9)]:
        assert abs(a - b) == max(a, b) - min(a, b)
wa, wb = QUOTED["warning_pair"]
assert max(wa, wb) == QUOTED["warning_max"] != wb
for y in [Fr(k, 7) for k in range(-50, 51)]:
    xw = y + 1 if y >= 0 else Fr(0)
    assert xw**2 > y
for xv in [Fr(k, 5) for k in range(-20, 21)]:
    assert not (xv**2 > xv**2)     # y = x^2 refutes exists x forall y
print("exm-rhetoric-induction: all quoted values check")
