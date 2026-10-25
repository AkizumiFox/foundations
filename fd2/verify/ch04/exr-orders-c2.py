"""exr-orders-c2: the least positive ka + lb equals gcd(a, b) (a, b in 0..20, not both 0), and is
the infimum under divisibility; sups of finite sets under | are lcms; no c in Z_{>0} is divisible by
c + 1."""
from math import gcd, lcm
from functools import reduce

QUOTED = {}  # (C2 quotes no numbers; the checks below test its claims on samples)
SAMPLE_SETS = ([4, 6, 10], [3, 5], [7], [2, 3, 4, 5, 6])

for a in range(0, 21):
    for b in range(0, 21):
        if a == 0 and b == 0:
            continue
        D = {k * a + l * b for k in range(-25, 26) for l in range(-25, 26)} 
        d = min(x for x in D if x > 0)
        assert d == gcd(a, b) and a % d == 0 and b % d == 0
        divs = [c for c in range(1, 41) if a % c == 0 and b % c == 0]
        assert all(d % c == 0 for c in divs)
for T in SAMPLE_SETS:
    L = reduce(lcm, T)
    ups = [c for c in range(0, 400) if all(c % t == 0 for t in T)]
    assert min(c for c in ups if c > 0) == L and all(c % L == 0 for c in ups)
divides = lambda t, c: c == 0 if t == 0 else c % t == 0
assert [c for c in range(0, 50) if all(divides(t, c) for t in [0, 3])] == [0]
assert not any(c % (c + 1) == 0 for c in range(1, 10000))
print("exr-orders-c2: all quoted values check")
