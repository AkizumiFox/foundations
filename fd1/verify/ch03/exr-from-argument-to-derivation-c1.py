"""exr-from-argument-to-derivation-c1 (Ch 3 s03): the sequent is valid; without G it breaks at n = 2."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403

QUOTED = {"break": 2, "lines": 14}
P, E, T, G = V("P"), V("E"), V("T"), V("G")
F1, F2 = Imp(And(P, E), Not(G)), Imp(And(P, T), Not(G))
assert classically_valid([G, Or(E, T), F1, F2], Not(P))
n = QUOTED["break"]
v = {"E": n % 2 == 0, "P": n > 1 and all(n % d for d in range(2, n)), "T": n % 3 == 0, "G": n > 10}
for f in [Or(E, T), F1, F2, Not(Not(P))]:
    assert tv(f, v) is True
assert tv(G, v) is False
print("exr-from-argument-to-derivation-c1: ok")
