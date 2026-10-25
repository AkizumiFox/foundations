"""Quick check after exm-squaring-mod-eleven: [a] -> [a^2 + 1] on Z/7 from [0]: 0, 1, 2, 5, 5; m = 3, p = 1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import tail_and_period

QUOTED = {"orbit": [0, 1, 2, 5, 5], "m": 3, "p": 1}
g = {a: (a * a + 1) % 7 for a in range(7)}
m, p, seq = tail_and_period(g, 0, 7)
assert seq[:5] == QUOTED["orbit"] and (m, p) == (QUOTED["m"], QUOTED["p"])
assert 26 - 21 == 5
print("prp-eventually-periodic: all quoted values check")
