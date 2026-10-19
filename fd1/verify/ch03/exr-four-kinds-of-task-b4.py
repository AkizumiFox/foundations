"""exr-four-kinds-of-task-b4 (Ch 3 s02): lists (a), (c), (e) are true under no assignment
(so a derivation of bot is consistent with the truth table); (b), (d), (f) are made true at
the stated statements; (f) with the fourth member not(not P and not Q) is true under none."""
from fractions import Fraction
from itertools import product


def imp(a, b):
    return (not a) or b


L = {
    "a": [lambda P, Q, R: imp(P, Q), lambda P, Q, R: imp(Q, not P), lambda P, Q, R: P],
    "b": [lambda P, Q, R: P or Q, lambda P, Q, R: imp(P, not Q), lambda P, Q, R: imp(Q, not P)],
    "c": [lambda P, Q, R: not imp(P, Q), lambda P, Q, R: Q or (not P)],
    "d": [lambda P, Q, R: imp(P, Q and not Q)],
    "e": [lambda P, Q, R: not (P or Q), lambda P, Q, R: P or (Q and R)],
    "f": [lambda P, Q, R: not (P and Q), lambda P, Q, R: not (P and not Q),
          lambda P, Q, R: not ((not P) and Q)],
}


def sat(members):
    return any(all(m(*v) for m in members) for v in product([False, True], repeat=3))


QUOTED = {"derive_bot": {"a", "c", "e"},
          "true_at": {"b": (Fraction(1) > 0, Fraction(1) < 0, False),   # x > 0, x < 0 at x = 1
                      "d": (0 == 1, False, False), "d2": (0 == 1, True, False),  # any Q
                      "f": (1 > 2, 2 > 3, False)},
          "lines": {"a": 6, "c": 11, "e": 10}}
for k, members in L.items():
    assert sat(members) == (k not in QUOTED["derive_bot"]), k
for k, v in QUOTED["true_at"].items():
    assert all(m(*v) for m in L[k[0]]), k
assert not sat(L["f"] + [lambda P, Q, R: not ((not P) and (not Q))])
print("exr-four-kinds-of-task-b4: ok")
