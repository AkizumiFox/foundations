"""exr-reductio-and-classical-rules-r2 (Ch 2 s05): balanced at 4, 6, 7, 9; the two forms agree for
|n| <= 500; the two directions classically valid; left-to-right classical (Kripke countermodel),
right-to-left without (no countermodel up to 3 worlds); at n = 7 the left disjunct fails and at
n = 6 the right."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
E, T = V("E"), V("T")

QUOTED = {"balanced": {4: False, 6: True, 7: True, 9: False}}
ev = lambda n: n % 2 == 0
th = lambda n: n % 3 == 0
for n, b in QUOTED["balanced"].items():
    assert (ev(n) == th(n)) == b
for n in range(-500, 501):
    assert (ev(n) == th(n)) == ((ev(n) and th(n)) or (not ev(n) and not th(n)))
L = Iff(E, T)
Rt = Or(And(E, T), And(Not(E), Not(T)))
assert classically_valid([L], Rt) and classically_valid([Rt], L)
assert kripke_refutation([L], Rt) is not None
assert kripke_refutation([Rt], L) is None
assert not (ev(7) and th(7)) and (not ev(7) and not th(7))
assert (ev(6) and th(6)) and not (not ev(6) and not th(6))
print("exr-reductio-and-classical-rules-r2: ok")
