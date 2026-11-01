"""exm-squaring-mod-eleven: forward orbit of [2] under squaring on Z/11; m = 1, p = 4; s(2) = s(9)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import tail_and_period

QUOTED = {"orbit": [2, 4, 5, 3, 9, 4], "m": 1, "p": 4, "cycle": {4, 5, 3, 9}}
s = {a: (a * a) % 11 for a in range(11)}
m, p, seq = tail_and_period(s, 2, 11)
assert seq[:6] == QUOTED["orbit"] and (m, p) == (QUOTED["m"], QUOTED["p"])
assert 16 - 11 == 5 and 25 - 22 == 3 and 81 - 77 == 4
assert s[2] == s[9] == 4
x, later = 2, []
for _ in range(200):
    x = s[x]
    later.append(x)
assert set(later) == QUOTED["cycle"] and 2 not in later
print("exm-squaring-mod-eleven: all quoted values check")
