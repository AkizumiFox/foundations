"""exr-four-kinds-of-task-b3 (Ch 3 s02, derive or break): the nine verdicts by truth table
(b, c, e, h, i derive; a, d, f, g break), and each break at its stated real x."""
from fractions import Fraction
from itertools import product


def imp(a, b):
    return (not a) or b


def valid(prem, concl):
    return all(concl(*v) for v in product([False, True], repeat=3) if all(p(*v) for p in prem))


C = {
    "a": ([lambda P, Q, R: (not P) or (not Q)], lambda P, Q, R: not (P or Q)),
    "b": ([lambda P, Q, R: not (P == Q), lambda P, Q, R: P], lambda P, Q, R: not Q),
    "c": ([lambda P, Q, R: imp(P, Q), lambda P, Q, R: imp(not P, R or Q), lambda P, Q, R: not R],
          lambda P, Q, R: Q),
    "d": ([lambda P, Q, R: imp(P, Q), lambda P, Q, R: imp(not P, R or Q), lambda P, Q, R: not R],
          lambda P, Q, R: P),
    "e": ([lambda P, Q, R: imp(imp(P, Q), R), lambda P, Q, R: not R], lambda P, Q, R: P),
    "f": ([lambda P, Q, R: imp(imp(P, Q), R), lambda P, Q, R: not R], lambda P, Q, R: Q),
    "g": ([lambda P, Q, R: P or Q, lambda P, Q, R: P], lambda P, Q, R: not Q),
    "h": ([lambda P, Q, R: P or Q, lambda P, Q, R: not (P and Q), lambda P, Q, R: P],
          lambda P, Q, R: not Q),
    "i": ([lambda P, Q, R: imp(not (P or Q), P)], lambda P, Q, R: P or Q),
}
F = lambda x: False
QUOTED = {
    "derive": {"b", "c", "e", "h", "i"},
    "breaks": {  # (P, Q, R) as statements about x, and the x
        "a": ((lambda x: x > 2, lambda x: x > 0, F), 1),
        "d": ((lambda x: x > 5, lambda x: x > 0, lambda x: x > 10), 1),
        "f": ((lambda x: x > 0, lambda x: x > 2, lambda x: x > 3), 1),
        "g": ((lambda x: x > 1, lambda x: x > 2, F), 3),
    },
    "lines": {"b": 10, "c": 10, "e": 7, "h": 7, "i": 6},
}
for k, (prem, concl) in C.items():
    assert valid(prem, concl) == (k in QUOTED["derive"]), k
for k, (stmts, x) in QUOTED["breaks"].items():
    v = [s(Fraction(x)) for s in stmts]
    prem, concl = C[k]
    assert all(p(*v) for p in prem) and not concl(*v), k
print("exr-four-kinds-of-task-b3: ok")
