"""A1 (c): x = (3,4), y = (4,3): u = (3/5,4/5), v = (4/5,3/5), <u,v> = 24/25, ||u-v||^2 = 2/25 = 2 - 48/25, <x,y> = 24 <= 25."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _common_ch09_05 import *
QUOTED = {"u": (Fr(3, 5), Fr(4, 5)), "v": (Fr(4, 5), Fr(3, 5)), "uv": Fr(24, 25), "umv2": Fr(2, 25), "xy": 24, "prod": 25}
x, y = (3, 4), (4, 3)
assert n2(x) == 25 == n2(y)
u, v = sc(Fr(1, 5), x), sc(Fr(1, 5), y)
assert u == QUOTED["u"] and v == QUOTED["v"] and n2(u) == 1 == n2(v)
assert dot(u, v) == QUOTED["uv"]
assert n2(add(u, sc(-1, v))) == QUOTED["umv2"] == 2 - 2 * QUOTED["uv"] == Fr(1, 25) + Fr(1, 25)
assert n2(add(u, v)) == 2 + 2 * QUOTED["uv"]
assert dot(x, y) == QUOTED["xy"] == 25 * QUOTED["uv"] and QUOTED["xy"] <= QUOTED["prod"]
print("ok")
