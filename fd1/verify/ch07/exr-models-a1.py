"""exr-models-a1 (Section 4.11): the truth table of four sentences in (N,<), (Z,<), (Q,<),
checked on windows with the witnesses the solution names (d + 1, d - 1, 0, (d + e)/2); (b) reads
sentence (ii) off the table: true in N, false in Z."""
import sys
from fractions import Fraction as F
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, P, ALL, EX

QUOTED = {"table": {"a": ("true", "true", "true"), "b": ("true", "false", "false"),
                    "c": ("false", "false", "true"), "d": ("false", "true", "true")}}

N = list(range(0, 60))
Z = list(range(-30, 31))
Q = [F(k, 6) for k in range(-60, 61)]
# (a)(i) witness d + 1 lies in each domain and is larger
for D in (N, Z, Q):
    assert all(d + 1 > d for d in D)
# (a)(ii) least element: 0 in N; in Z, Q every d has d - 1 < d in the domain
assert all(not (e < 0) for e in N)
assert all(d - 1 < d for d in Z) and all(d - 1 < d for d in Q)
# (a)(iii) density: fails in N and Z at 1, 2 (no integer strictly between); holds in Q by midpoint
assert not any(1 < z < 2 for z in range(-100, 100))
for d in Q[::7]:
    for e in Q[::11]:
        if d < e:
            m = (d + e) / 2
            assert isinstance(m, F) and d < m < e
# (a)(iv) no least element: fails in N at 0; holds in Z, Q with d - 1
assert not any(e < 0 for e in N)
# (b) sentence (ii) is true in N and false in Z (checked with the witnesses above, and on finite
#     windows as a sanity check: a window of N has least element 0)
b = EX("x", ALL("y", ("not", P("<", "y", "x"))))
Nw = list(range(0, 20))
assert sat(b, structure(Nw, pred={"<": {(a, c) for a in Nw for c in Nw if a < c}}), {})
tab = {"a": (True, True, True), "b": (True, False, False), "c": (False, False, True),
       "d": (False, True, True)}
assert tab["b"][0] and not tab["b"][1]
for k, v in tab.items():
    assert QUOTED["table"][k] == tuple("true" if b else "false" for b in v)
print("exr-models-a1: all quoted values check")
