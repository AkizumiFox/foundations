"""exr-from-argument-to-derivation-b4 (Ch 3 s03): a <= 1, b <= 1 give a + b <= 2 (grid); the distractor
(iii) fails at a = 0, b = 3; the derivation's sequent is valid."""
import sys
from fractions import Fraction as Fr
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403

QUOTED = {"a": 0, "b": 3}
grid = [Fr(k, 4) for k in range(-40, 41)]
for a in grid:
    for b in grid:
        if a <= 1 and b <= 1:
            assert a + b <= 2
a, b = QUOTED["a"], QUOTED["b"]
assert a + b > 2 and a <= 1
A, B, S = V("A"), V("B"), V("S")
assert classically_valid([Imp(And(Not(A), Not(B)), Not(S))], Imp(S, Or(A, B)))
print("exr-from-argument-to-derivation-b4: ok")
