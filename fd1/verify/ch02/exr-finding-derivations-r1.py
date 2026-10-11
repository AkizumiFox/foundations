"""exr-finding-derivations-r1 (Ch 2 s06): max(a, b) + min(a, b) = a + b, with the item's definitions."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}
from itertools import product as _p
def mx(a, b): return a if a >= b else b
def mn(a, b): return b if a >= b else a
vals = [Fraction(n, 3) for n in range(-7, 8)]
for a, b in _p(vals, vals):
    assert mx(a, b) + mn(a, b) == a + b
print("exr-finding-derivations-r1: ok")
