"""exr-reductio-and-classical-rules-b5 (Ch 2 s05, derive or break): the eight verdicts by truth
table; the breaks (b), (d), (g) at x = 1; the side-breaks quoted in (c) (x = 4, x = 0) and (h)
(x = 1); (a) needs no classical rule (no Kripke countermodel up to 3 worlds is found, and its printed
derivation has no RAA); the derivations of (c), (f), (h) are classical (Kripke countermodels)."""
import sys
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R = V("P"), V("Q"), V("R")

claims = {
    "a": ([Or(P, Q), Or(Not(P), R)], Or(Q, R)),
    "b": ([Not(And(P, Q))], And(Not(P), Not(Q))),
    "c": ([Imp(P, Q)], Or(Iff(P, Q), Q)),
    "d": ([Or(Imp(P, Q), Imp(P, R))], Imp(P, And(Q, R))),
    "e": ([Or(Not(Not(P)), Q)], Or(P, Q)),
    "f": ([Not(Iff(P, Q))], Iff(P, Not(Q))),
    "g": ([Not(Iff(P, Q))], And(Not(P), Q)),
    "h": ([Imp(And(P, Q), R)], Or(Imp(P, R), Imp(Q, R))),
}
QUOTED = {
    "verdicts": {"a": "derive", "b": "break", "c": "derive", "d": "break", "e": "derive",
                 "f": "derive", "g": "break", "h": "derive"},
    "breaks": {"b": ({"P": lambda x: x > 0, "Q": lambda x: x > 5}, 1),
               "d": ({"P": lambda x: x > 0, "Q": lambda x: x > -1, "R": lambda x: x > 5}, 1),
               "g": ({"P": lambda x: x > 0, "Q": lambda x: x > 5}, 1)},
    "lines": {"a": 12, "c": 13, "e": 7, "f": 22, "h": 14},
}
for k, (prem, concl) in claims.items():
    assert classically_valid(prem, concl) == (QUOTED["verdicts"][k] == "derive"), k
for k, (stmts, x) in QUOTED["breaks"].items():
    prem, concl = claims[k]
    v = {n: f(Fraction(x)) for n, f in stmts.items()}
    assert all(tv(p, v) for p in prem) and not tv(concl, v), k
# (c): each side breaks on its own, P: x > 5, Q: x > 3; the premise holds at every x
p, q = (lambda x: x > 5), (lambda x: x > 3)
for k in range(-200, 201):
    x = Fraction(k, 10)
    assert (not p(x)) or q(x)
assert p(4) != q(4)          # P <-> Q fails at x = 4
assert not q(0)              # Q fails at x = 0
# (h): P: x > 0, Q: x > 5, R: x > 3; premise at every x; P -> R fails at x = 1; swapped, Q -> R fails
p, q, r = (lambda x: x > 0), (lambda x: x > 5), (lambda x: x > 3)
for k in range(-200, 201):
    x = Fraction(k, 10)
    assert (not (p(x) and q(x))) or r(x)
    assert (not (q(x) and p(x))) or r(x)
assert p(1) and not r(1)
# classical status of the derivations
assert kripke_refutation(*claims["a"]) is None
for k in ("c", "f", "h"):
    assert kripke_refutation(*claims[k]) is not None, k
print("exr-reductio-and-classical-rules-b5: ok")
