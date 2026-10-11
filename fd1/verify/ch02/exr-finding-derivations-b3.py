"""exr-finding-derivations-b3 (Ch 2 s06): the sequent is valid and derivable without RAA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}
seq = ([Imp(P, Imp(Q, R)), Imp(P, Imp(R, S))], Imp(P, Imp(Q, S)))
assert classically_valid(*seq)
assert kripke_refutation(*seq) is None
print("exr-finding-derivations-b3: ok")
