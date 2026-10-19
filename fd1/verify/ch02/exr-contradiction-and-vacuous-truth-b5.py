"""exr-contradiction-and-vacuous-truth-b5 (Ch 2, Section 2.1): derive or break. Each verdict by
truth table (derive: every assignment making the premises true makes the conclusion true; break:
some assignment does not), and each break at its stated number makes every member of the
counterexample set (premises and the negated conclusion) true; where the text says a premise holds
for every x, it is checked on a grid of exact rationals."""
from fractions import Fraction as F
from itertools import product

imp = lambda a, b: (not a) or b
CLAIMS = {  # premises, conclusion as functions of (P, Q, R, S); verdict
    "a": (lambda P, Q, R, S: [(P and not Q) or R, Q], lambda P, Q, R, S: R, "derive"),
    "b": (lambda P, Q, R, S: [P or Q, not Q], lambda P, Q, R, S: not P, "break"),
    "c": (lambda P, Q, R, S: [imp(P, not P), P], lambda P, Q, R, S: Q, "derive"),
    "d": (lambda P, Q, R, S: [imp(P, Q), not P], lambda P, Q, R, S: not Q, "break"),
    "e": (lambda P, Q, R, S: [not (P and Q), P], lambda P, Q, R, S: imp(Q, R), "derive"),
    "f": (lambda P, Q, R, S: [not (P and Q)], lambda P, Q, R, S: (not P) or Q, "break"),
    "g": (lambda P, Q, R, S: [P or Q, imp(P, R), not R], lambda P, Q, R, S: P, "break"),
    "h": (lambda P, Q, R, S: [imp(P, Q and not R), R], lambda P, Q, R, S: imp(P, S), "derive"),
}
for k, (prem, concl, verdict) in CLAIMS.items():
    valid = all(concl(*v) for v in product([False, True], repeat=4) if all(prem(*v)))
    assert valid == (verdict == "derive"), k

QUOTED = {"b": 1, "d": 2, "f": 1, "g": 1}
grid = [F(p, q) for p in range(-200, 201) for q in (1, 2, 3, 7)]


def counterexample_true(k, P, Q, R=False, S=False):
    prem, concl, _ = CLAIMS[k]
    return all(prem(P, Q, R, S)) and not concl(P, Q, R, S)


# (b) P: x > 0, Q: x > 5 at x = 1
x = F(QUOTED["b"]); assert counterexample_true("b", x > 0, x > 5)
# (d) P: x > 3, Q: x > 1 at x = 2; P -> Q for every x
x = F(QUOTED["d"]); assert counterexample_true("d", x > 3, x > 1)
assert all(imp(t > 3, t > 1) for t in grid)
# (f) P: x > 0, Q: x > 5 at x = 1
x = F(QUOTED["f"]); assert counterexample_true("f", x > 0, x > 5)
# (g) P: x > 5, Q: x > 0, R: x > 3 at x = 1; P -> R for every x
x = F(QUOTED["g"]); assert counterexample_true("g", x > 5, x > 0, x > 3)
assert all(imp(t > 5, t > 3) for t in grid)
print("exr-contradiction-and-vacuous-truth-b5: all verdicts and witnesses check")
