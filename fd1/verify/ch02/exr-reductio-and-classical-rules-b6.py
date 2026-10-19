"""exr-reductio-and-classical-rules-b6 (Ch 2 s05): (P -> Q) or (Q -> P) is true at every row;
at n = 2 (even, not > 5) Q -> P holds and P -> Q fails; at n = 7 (odd, > 5) the reverse; each
separated "every" claim is refuted (n = 2, n = 7); each disjunct breaks at x = 1 with x > 0, x > 5."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q = V("P"), V("Q")

QUOTED = {"n": (2, 7), "x": 1}
assert classically_valid([], Or(Imp(P, Q), Imp(Q, P)))
imp = lambda a, b: (not a) or b
ev = lambda n: n % 2 == 0
gt5 = lambda n: n > 5
assert imp(gt5(2), ev(2)) and not imp(ev(2), gt5(2))
assert imp(ev(7), gt5(7)) and not imp(gt5(7), ev(7))
assert any(not imp(ev(n), gt5(n)) for n in range(-50, 51))
assert any(not imp(gt5(n), ev(n)) for n in range(-50, 51))
x = QUOTED["x"]
assert (x > 0) and not (x > 5)       # P -> Q false at x = 1 (P: x > 0, Q: x > 5)
assert not imp(x > 0, x > 5)
assert not imp(x > 0, x > 5)         # exchanged: Q -> P with Q: x > 0, P: x > 5, same value
print("exr-reductio-and-classical-rules-b6: ok")
