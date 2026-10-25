"""exr-naturals-and-well-ordering-a1 (Ch 7, 01): (c) the proof run on S = {4, 7, 9} meets S at n = 4;
(e) in N' = N u (N + 1/2): holds: (a) first clause, sum half of (b), (d); fails: (a) second clause
(1/2), product half of (b) (1/2 * 1/2 = 1/4), (c) (1/2 - 1 = -1/2), (e) (0 < 1/2 < 1).
Also Z u (Z + 1/2) has the predecessor property and contains 1/2 between 0 and 1."""
from fractions import Fraction as F

H = F(1, 2)
S = {4, 7, 9}
QUOTED = {"first_hit": 4, "quarter": F(1, 4)}
n = 0
while n not in S:
    n += 1
assert n == QUOTED["first_hit"] == min(S)

def inN(x):
    return x >= 0 and x.denominator in (1, 2)

K = 25
seg = [F(n) for n in range(K)] + [n + H for n in range(K)]
assert all(x >= 0 for x in seg)                                  # (a) first clause holds
assert any(x != 0 and not x >= 1 for x in seg) and H in seg      # (a) second clause fails at 1/2
assert all(inN(x + y) for x in seg for y in seg)                 # (b) sums hold
assert H * H == QUOTED["quarter"] and not inN(QUOTED["quarter"])  # (b) products fail
assert not inN(H - 1) and H - 1 == -H                            # (c) fails
assert all(inN(y - x) for x in seg for y in seg if x <= y)       # (d) holds
assert 0 < H < 1                                                 # (e) fails
# Z u (Z + 1/2): predecessor property on a segment
seg2 = [F(k) for k in range(-K, K)] + [k + H for k in range(-K, K)]
assert all((x - 1) in set(seg2) or x - 1 < -K for x in seg2 if x != 0)
print("exr-naturals-and-well-ordering-a1: all quoted values check")
