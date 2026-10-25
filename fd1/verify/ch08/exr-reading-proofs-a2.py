"""exr-reading-proofs-a2 (Section 8.4 drill) and the two lines of "Naming the unstated
fact": (a) n = 2k gives n^2 = 2(2k^2); (b) x^2 - 1 = (x - 1)(x + 1); (g) 0 < a < b gives
a*a < a*b < b*b; (h) |x - 2| < 1 iff 1 < x < 3, so x > 1; (i) x^2 = 9 and x > 0 give x = 3;
(k) x < 0 gives 1/x < 0; and: 3 | n^2 implies 3 | n (true), 4 | n^2 implies 4 | n (false
at n = 2)."""
from fractions import Fraction as Fr

QUOTED = {"counterexample n": 2}
for k in range(-100, 101):
    n = 2 * k
    assert n * n == 2 * (2 * k * k)
grid = [Fr(a, 9) for a in range(-90, 91)]
for x in grid:
    assert x * x - 1 == (x - 1) * (x + 1)
    if abs(x - 2) < 1:
        assert -1 < x - 2 and x > 1
    if x * x == 9 and x > 0:
        assert x == 3
    if x < 0:
        assert 1 / x < 0 and x * (1 / x) == 1
    if x > 1:
        assert x * x > x
for a in grid:
    for b in grid:
        if 0 < a < b:
            assert a * a < a * b < b * b
assert {x for x in range(-20, 21) if x * x == 9} == {3, -3}
for n in range(-300, 301):
    if (n * n) % 3 == 0:
        assert n % 3 == 0
n = QUOTED["counterexample n"]
assert (n * n) % 4 == 0 and n % 4 != 0
print("exr-reading-proofs-a2: all quoted values check")
