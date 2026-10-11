"""exr-reductio-and-classical-rules-b4 (Ch 2 s05): for real x, x > 1 gives x > 0 and x^2 > x."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}
for x in (Fraction(1001, 1000), Fraction(3, 2), Fraction(2), Fraction(17, 3), Fraction(10**6)):
    assert x > 1 and x > 0 and x * x > x and x * x - x == x * (x - 1)
print("exr-reductio-and-classical-rules-b4: ok")
