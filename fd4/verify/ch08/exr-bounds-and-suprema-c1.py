"""exr-bounds-and-suprema-c1: delta = eps/(2s); both cases; the counterexample on [-2, 1]."""
from fractions import Fraction as Fr

QUOTED = {"counter_sup_f": 1, "counter_sup_f2": 4}
for s in [Fr(1, 10), Fr(1, 2), Fr(1), Fr(3), Fr(50)]:
    for eps in [Fr(1, 1000), Fr(1, 10), Fr(1), Fr(5), Fr(200)]:
        d = eps / (2 * s)
        assert (s - d)**2 == s**2 - eps + d**2 > s**2 - eps
        if s - d < 0:
            assert s**2 < eps / 2 and s**2 - eps < -eps / 2 < 0
        # any witness value strictly between s - d and s (when admissible) squares above s^2 - eps
        for t in [max(s - d, Fr(0)) + (s - max(s - d, Fr(0))) * Fr(j, 7) for j in range(1, 8)]:
            if t > s - d and t >= 0:
                assert t * t > s**2 - eps
pts = [Fr(k, 100) for k in range(-200, 101)]
assert max(pts) == QUOTED["counter_sup_f"] and max(x * x for x in pts) == QUOTED["counter_sup_f2"]
print("ok")
