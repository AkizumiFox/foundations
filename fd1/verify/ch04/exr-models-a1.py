"""exr-models-a1 (Section 4.11): the truth table of four sentences in (N,<), (Z,<), (Q,<),
checked on windows with the witnesses the solution names (d + 1, d - 1, 0, (d + e)/2), plus the
{1, 2, 3} fact used in (e)."""
import sys
from fractions import Fraction as F
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, P, ALL, EX

QUOTED = {"table": {"a": ("true", "true", "true"), "b": ("true", "false", "false"),
                    "c": ("false", "false", "true"), "d": ("false", "true", "true")}}

N = list(range(0, 60))
Z = list(range(-30, 31))
Q = [F(k, 6) for k in range(-60, 61)]
# (a) witness d + 1 lies in each domain and is larger
for D in (N, Z, Q):
    assert all(d + 1 > d for d in D)
# (b) least element: 0 in N; in Z, Q every d has d - 1 < d in the domain
assert all(not (e < 0) for e in N)
assert all(d - 1 < d for d in Z) and all(d - 1 < d for d in Q)
# (c) density: fails in N and Z at 1, 2 (no integer strictly between); holds in Q by midpoint
assert not any(1 < z < 2 for z in range(-100, 100))
for d in Q[::7]:
    for e in Q[::11]:
        if d < e:
            m = (d + e) / 2
            assert isinstance(m, F) and d < m < e
# (d) no least element: fails in N at 0; holds in Z, Q with d - 1
assert not any(e < 0 for e in N)
# (e) forall x exists y (x < y) false in {1, 2, 3}
D3 = [1, 2, 3]
M3 = structure(D3, pred={"<": {(a, b) for a in D3 for b in D3 if a < b}})
assert not sat(ALL("x", EX("y", P("<", "x", "y"))), M3, {})
tab = {"a": (True, True, True), "b": (True, False, False), "c": (False, False, True),
       "d": (False, True, True)}
for k, v in tab.items():
    assert QUOTED["table"][k] == tuple("true" if b else "false" for b in v)
print("exr-models-a1: all quoted values check")
