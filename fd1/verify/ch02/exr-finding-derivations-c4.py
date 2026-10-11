"""exr-finding-derivations-c4 (Ch 2 s06): (a) needs no RAA; (b) is valid and its derivation uses RAA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}
a = ([Not(And(P, Q)), P], Not(Q))
b = ([Not(And(P, Not(Q))), P], Q)
assert classically_valid(*a) and classically_valid(*b)
assert kripke_refutation(*a) is None
assert kripke_refutation(*b) is not None
print("exr-finding-derivations-c4: ok")
