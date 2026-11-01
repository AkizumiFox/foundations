"""exr-roots-and-rational-powers-c1 (05): for 0 < a < 1, r < s gives a^r > a^s, and r > 0 gives a^r < 1 (exact, a = c^60)."""
from fractions import Fraction as F

QUOTED = {}
L = 60
rs = [F(p, q) for p in range(-5, 6) for q in (1, 2, 3, 4, 5)]
for c in [F(1, 2), F(2, 3), F(9, 10)]:
    for r in rs:
        ar = c ** int(r * L)
        for s in rs:
            if r < s:
                assert ar > c ** int(s * L)
        if r > 0:
            assert ar < 1
print("ok")
