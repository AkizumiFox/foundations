"""exr-from-argument-to-derivation-r4 (Ch 3 s03): the dialogue's three facts on a grid of reals;
x^2 < x exactly when 0 < x < 1 on the grid; the sequent is valid."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403

QUOTED = {"lines": 10}
for k in range(-400, 401):
    x = Fr(k, 64)
    L = x * x < x
    if x < 0:
        assert x * x > 0 > x and not L
    if x == 0:
        assert x * x == x and not L
    if x >= 1:
        assert x > 0 and x * x >= x and not L
    assert L == (0 < x < 1)
N, Z, B, L = V("N"), V("Z"), V("B"), V("L")
assert classically_valid([Imp(N, Not(L)), Imp(Z, Not(L)), Imp(B, Not(L)), L],
                         And(And(Not(N), Not(Z)), Not(B)))
print("exr-from-argument-to-derivation-r4: ok")
