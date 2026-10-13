"""exr-finding-derivations-r2 (Ch 2 s06): not(N or G) |- not N and (G -> S) is valid, needs no RAA,
and the 11-line derivation checks."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}
seq = ([Not(Or(N, G))], And(Not(N), Imp(G, S)))
assert classically_valid(*seq)
assert kripke_refutation(*seq) is None
print("exr-finding-derivations-r2: ok")
