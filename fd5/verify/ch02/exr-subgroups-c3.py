"""exr-subgroups-c3: mZ subset nZ iff n | m, and mZ cap nZ = LZ with L the least positive
common multiple, on a window of m, n."""
from math import lcm
QUOTED = {}  # no numeric value is quoted in the text; structural brute-force check only
for m in range(1, 25):
    for n in range(1, 25):
        win = range(-300, 301)
        mZ = {k for k in win if k % m == 0}
        nZ = {k for k in win if k % n == 0}
        inner = {k for k in range(-100, 101) if k % m == 0}
        assert (inner <= nZ) == (m % n == 0)
        L = min(k for k in range(1, m * n + 1) if k % m == 0 and k % n == 0)
        assert L == lcm(m, n)
        assert {k for k in range(-100, 101) if k in mZ and k in nZ} == {k for k in range(-100, 101) if k % L == 0}
print("exr-subgroups-c3: ok")
