"""exm-derive-or-break-search (Ch 3 s02): (a) valid by truth table, (b) invalid, broken at
P, Q true, R false and at x = 2 with P: x > 0, Q: x > 1, R: x > 3.  The Quick check's
one-symbol repairs of (b)'s first premise (or -> implies, and, iff; Q -> R) are all valid."""
from fractions import Fraction
from itertools import product


def imp(a, b):
    return (not a) or b


def valid(prem, concl):
    return all(concl(*v) for v in product([False, True], repeat=3) if all(p(*v) for p in prem))


second = lambda P, Q, R: imp(P, not R)
concl = lambda P, Q, R: imp(P, not Q)
claims = {
    "a": lambda P, Q, R: imp(P, imp(Q, R)),
    "b": lambda P, Q, R: imp(P, Q or R),
    "repair_and": lambda P, Q, R: imp(P, Q and R),
    "repair_iff": lambda P, Q, R: imp(P, Q == R),
    "repair_R_for_Q": lambda P, Q, R: imp(P, R or R),
}
QUOTED = {"valid": {"a": True, "b": False, "repair_and": True, "repair_iff": True,
                    "repair_R_for_Q": True},
          "break_b": (True, True, False), "x": 2, "lines_a": 10, "lines_and": 9}
for k, first in claims.items():
    assert valid([first, second], concl) == QUOTED["valid"][k], k
P, Q, R = QUOTED["break_b"]
assert claims["b"](P, Q, R) and second(P, Q, R) and not concl(P, Q, R)
x = Fraction(QUOTED["x"])
assert (x > 0, x > 1, x > 3) == QUOTED["break_b"]
print("exm-derive-or-break-search: ok")
