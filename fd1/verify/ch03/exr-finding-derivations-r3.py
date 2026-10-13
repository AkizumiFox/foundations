"""exr-finding-derivations-r3 (Ch 2 s06): the sequent is valid; the converse fails at P = R = false."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"row": {"P": False, "R": False}}
assert classically_valid([Imp(Imp(P, Q), R)], Imp(P, Imp(Q, R)))
for q in (False, True):
    v = dict(QUOTED["row"], Q=q)
    assert tv(Imp(P, Imp(Q, R)), v) is True and tv(Imp(Imp(P, Q), R), v) is False
print("exr-finding-derivations-r3: ok")
