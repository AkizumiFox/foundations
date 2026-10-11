"""def-rules-universal (Ch 4, Section 4.4): the readings in "Why each clause", the
quick check, the warning, and the algebra of "How this rule looks"."""
from fractions import Fraction as Fr

QUOTED = {"premise: x_0 names": 2, "counterexample to every integer even": 1,
          "assumption: y": 1, "assumption: x": 0,
          "quick check: c": 0, "quick check: y_0": 1, "warning: n": 1}

even = lambda n: n % 2 == 0
# Premise clause: P(x_0) true with x_0 = 2; forall x P(x) false at 1.
assert even(QUOTED["premise: x_0 names"]) and not even(QUOTED["counterexample to every integer even"])
# Open-assumption clause: at y = 1, 1 > 0 holds and x > 0 fails at x = 0.
assert QUOTED["assumption: y"] > 0 and not (QUOTED["assumption: x"] > 0)
# Conclusion clause: over N, forall x (x <= x) true; forall x (x <= y_0) fails at y_0 + 1.
assert all(n <= n for n in range(1000))
assert all(not (y0 + 1 <= y0) for y0 in range(1000))
# Quick check: over Z, R(x, y) := x != y is symmetric; R(0, 1) holds; forall y (y != 0) fails at 0.
Z = range(-50, 50)
assert all((x != y) == (y != x) for x in Z for y in Z)
assert QUOTED["quick check: c"] != QUOTED["quick check: y_0"]
assert not all(y != QUOTED["quick check: c"] for y in Z)
# Warning: n = 1 is odd, and 1^2 is odd.
n = QUOTED["warning: n"]
assert not even(n) and not even(n * n)
# How this rule looks: (x - 1)^2 = x^2 - 2x + 1, at many exact points (degree 2).
assert all((t - 1) ** 2 == t * t - 2 * t + 1 for t in [Fr(k, 11) for k in range(-100, 100)])
print("def-rules-universal: all quoted values check")
