"""exr-reductio-and-classical-rules-r3 (Ch 2 s05): P: n multiple of 6, Q: n even; P -> Q for every n;
at n = 2 the steps to (ii) Q -> P, (iii) not P -> not Q, (vi) P <-> Q break; (i), (iv), (v) are
classically valid consequences; (iv)'s classical status (Kripke countermodel), (v) without."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q = V("P"), V("Q")

QUOTED = {"n": 2}
for n in range(-600, 601):
    assert (n % 6 != 0) or (n % 2 == 0)
n = QUOTED["n"]
v = {"P": n % 6 == 0, "Q": n % 2 == 0}
assert tv(Imp(P, Q), v)
for f in (Imp(Q, P), Imp(Not(P), Not(Q)), Iff(P, Q)):
    assert not tv(f, v)
for f in (Imp(Not(Q), Not(P)), Or(Not(P), Q), Imp(P, And(P, Q))):
    assert classically_valid([Imp(P, Q)], f)
assert kripke_refutation([Imp(P, Q)], Or(Not(P), Q)) is not None
assert kripke_refutation([Imp(P, Q)], Imp(P, And(P, Q))) is None
print("exr-reductio-and-classical-rules-r3: ok")
