"""prp-contrapositive-converse (Ch 2 s05): valid; the text's "no derivation avoids RAA" is stated
without proof. Internal witness (not in the text): a two-world Kripke counter-model."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}
seq = ([Imp(Not(Q), Not(P))], Imp(P, Q))
assert classically_valid(*seq)
assert kripke_refutation(*seq) is not None
assert kripke_refutation([Imp(P, Q)], Imp(Not(Q), Not(P))) is None   # CP itself needs no RAA
print("prp-contrapositive-converse: ok")
