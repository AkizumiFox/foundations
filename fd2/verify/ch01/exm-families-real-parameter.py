"""exm-families-real-parameter (Section 6.2): witnesses t = x/2 and t = |x|, and the endpoint non-example."""
from fractions import Fraction as F
QUOTED = {}
pts = [F(n, 37) for n in range(-80, 81)]
# (a) union over t in (0,1) of [t,1] is (0,1]: witness t = x/2
for x in pts:
    if 0 < x <= 1:
        t = x / 2
        assert 0 < t < 1 and t <= x <= 1
# (a) every member lies in (0,1]
for t in [F(k, 50) for k in range(1, 50)]:
    for x in pts:
        if t <= x <= 1:
            assert 0 < x <= 1
# (b) t = |x| excludes x != 0 from (-t, t); 0 in every (-t, t)
for x in pts:
    if x != 0:
        t = abs(x)
        assert t > 0 and not (-t < x < t)
assert all(-t < 0 < t for t in [F(k, 9) for k in range(1, 100)])
# (c) t = 1 forces x > 0, then t = x excludes x from (0, x)
for x in pts:
    if 0 < x < 1:
        assert not (0 < x < x)
# non-example: 0 in every [0, t); x < 0 excluded by [0,1); x > 0 by [0, x)
for x in pts:
    if x < 0:
        assert not (0 <= x < 1)
    if x > 0:
        assert not (0 <= x < x)
# quick check: union over t in [1,2] of [0,t] is [0,2], intersection [0,1]
ts = [1 + F(k, 20) for k in range(21)]
for x in pts:
    assert (any(0 <= x <= t for t in ts)) == (0 <= x <= 2)
    assert (all(0 <= x <= t for t in ts)) == (0 <= x <= 1)
print("exm-families-real-parameter: all quoted values check")
