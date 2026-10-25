"""Quick check after exm-three-pile-shuffle: orbit of [1] under the tick (length 12) and under +3 (length 4)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _perm import orbits

QUOTED = {"tick_len": 12, "plus3": [1, 4, 7, 10]}
tick = {a: (a + 1) % 12 for a in range(12)}
plus3 = {a: (a + 3) % 12 for a in range(12)}
o = [o for o in orbits(tick, range(12)) if 1 in o][0]
assert len(o) == QUOTED["tick_len"]
assert [o for o in orbits(plus3, range(12)) if 1 in o][0] == QUOTED["plus3"]
assert orbits(tick, range(12))[0] == list(range(12))  # tick is the 12-cycle ([0] ... [11])
print("exm-method-follow-the-orbit: all quoted values check")
