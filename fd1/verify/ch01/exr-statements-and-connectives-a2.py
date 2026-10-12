"""Values quoted in the solution of exr-statements-and-connectives-a2 (Section 1.1, drill of 15 parts)."""
import sys, pathlib, itertools
from fractions import Fraction as Fr
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid, implies_on_grid

QUOTED = {"(f) x both": Fr(5, 2), "(f) x one": 4, "(g),(h) x": -2, "(i) n": 2, "(j) x": 0,
          "(n) all true": 8, "(n) breaks": 6, "(o) x": -2}
imp = lambda p, q: (not p) or q
one = lambda p, q: (p or q) and not (p and q)

x = QUOTED["(f) x both"]; assert x >= 2 and x <= 3 and not one(x >= 2, x <= 3)
x = QUOTED["(f) x one"];  assert x >= 2 and not x <= 3 and one(x >= 2, x <= 3)
x = QUOTED["(g),(h) x"]
assert not x > 1                               # (g): hypothesis false, nothing promised
assert x**2 > 1 and x**2 == 4 and not x > 1    # (h): broken
n = QUOTED["(i) n"]
assert all(n % d for d in range(2, n)) and n >= 2 and n % 2 == 0
x = QUOTED["(j) x"]
assert (x >= 0 or x <= 0) and x >= 0 and x <= 0
# (k): 7 is odd, so the premise "7 is even" is false; 49 is odd, so the conclusion is false
assert 7 % 2 == 1 and 49 % 2 == 1
# (l)(i): 2 > 3 false, the implication true, 3 odd
assert not 2 > 3 and imp(2 > 3, 3 % 2 == 1) and 3 % 2 == 1
# (l)(ii): P -> Q and P are never both false
assert not any((not imp(p, q)) and (not p) for p, q in itertools.product([True, False], repeat=2))
# (m): a good form (modus ponens) has no valuation with true premises and false conclusion
assert not any(imp(p, q) and p and not q for p, q in itertools.product([True, False], repeat=2))
# (n): P: divisible by 4, Q: even, R: > 0
P, Q, R = (lambda n: n % 4 == 0), (lambda n: n % 2 == 0), (lambda n: n > 0)
assert all(imp(P(n), Q(n)) for n in range(-200, 201))
n = QUOTED["(n) all true"]; assert P(n) and Q(n) and R(n) and imp(R(n), P(n)) and n == 4 * 2
n = QUOTED["(n) breaks"];   assert imp(P(n), Q(n)) and imp(Q(n), R(n)) and R(n) and not P(n)
# (o): P: x > 5, Q: x > 3, R: x < 0
assert implies_on_grid(lambda x: x > 5, lambda x: x > 3)
x = QUOTED["(o) x"]; assert imp(x > 5, x > 3) and (x > 5 or x < 0) and not x > 3
print("exr-statements-and-connectives-a2: checks")
