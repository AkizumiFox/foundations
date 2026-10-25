"""exr-sets-and-subsets-b4: Prove or disprove (verdicts and counterexamples)."""
from itertools import combinations, product
from fractions import Fraction as F

QUOTED = {"(b) witness": 4, "(c) set": {-1, 0, 1}, "(d) A": set(), "(d) B": {1}, "(d) C": set()}
R = range(-200, 201)
# (a) true: the two sets agree on a window, and the re-indexing identities hold
left = {n for n in R if any(n == 2 * k + 1 for k in range(-150, 150))}
right = {n for n in R if any(n == 2 * k - 1 for k in range(-150, 150))}
assert left == right
assert all(2 * (k + 1) - 1 == 2 * k + 1 and 2 * (k - 1) + 1 == 2 * k - 1 for k in range(-100, 101))
# (b) false: 4 is in the left set, not in the right
w = QUOTED["(b) witness"]
assert w % 2 == 0 and w % 4 == 0 and w % 8 != 0
assert w == 2 * 2 == 4 * 1
assert not any(8 * kk == 4 for kk in range(-100, 101))
# (c) true: real roots of x^3 - x
samples = [F(n, d) for n in range(-30, 31) for d in range(1, 8)]
assert all(x**3 - x == x * (x - 1) * (x + 1) for x in samples)  # cubic identity at > 4 points
assert {x for x in samples if x**3 == x} == QUOTED["(c) set"]
# (d) false: the counterexample
A, B, C = QUOTED["(d) A"], QUOTED["(d) B"], QUOTED["(d) C"]
assert A <= B and not B <= C and A <= C
# (e) true on all triples of subsets of a 3-element universe
subs = [frozenset(c) for n in range(4) for c in combinations([1, 2, 3], n)]
assert all(A == C for A, B, C in product(subs, repeat=3) if A <= B and B <= C and C <= A)
print("exr-sets-and-subsets-b4: all quoted values check")
