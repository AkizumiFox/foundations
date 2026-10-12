"""Forms, the break and the arithmetic of exr-statements-and-connectives-b6 (Section 1.1)."""
import sys, pathlib, itertools
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import implies_on_grid

QUOTED = {"break n": 2, "(a) x": -3, "12 =": (3, 4)}
imp = lambda p, q: (not p) or q
B = [True, False]
# (T)'s form P->Q, P->R / Q->R is bad; (c) P->Q, Q->R / P->R and (d) P->Q, P->R / P->(Q&R) are good
assert any(imp(p, q) and imp(p, r) and not imp(q, r) for p, q, r in itertools.product(B, repeat=3))
for p, q, r in itertools.product(B, repeat=3):
    assert not (imp(p, q) and imp(q, r) and not imp(p, r))
    assert not (imp(p, q) and imp(p, r) and not imp(p, q and r))
# the break: P: 6 | n, Q: 2 | n, R: 3 | n
P, Q, R = (lambda n: n % 6 == 0), (lambda n: n % 2 == 0), (lambda n: n % 3 == 0)
assert all(imp(P(n), Q(n)) and imp(P(n), R(n)) for n in range(-60, 61))
n = QUOTED["break n"]; assert Q(n) and not R(n) and not imp(Q(n), R(n))
# (a) at x = -3
assert implies_on_grid(lambda x: x > 2, lambda x: x**2 > 4) and implies_on_grid(lambda x: x > 2, lambda x: x > 1)
x = QUOTED["(a) x"]; assert x**2 == 9 > 4 and not x > 1
# (T)'s conclusion
a, b = QUOTED["12 ="]; assert a * b == 12 and Q(12) and R(12) and P(12)
print("exr-statements-and-connectives-b6: checks")
