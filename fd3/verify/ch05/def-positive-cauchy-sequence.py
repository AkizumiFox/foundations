"""def-positive-cauchy-sequence (examples): a_n = 1 - 2/(n+1) has first terms -1, 0, 1/3, 1/2;
a_n >= 1/2 for n >= 3 and a_2 = 1/3 < 1/2 (so N = 3 is least for delta = 1/2);
for 1/(n+1), every rational margin is undercut beyond every threshold."""
from fractions import Fraction as F
QUOTED = {"first": [F(-1), F(0), F(1, 3), F(1, 2)], "delta": F(1, 2), "N": 3, "a2": F(1, 3)}
a = lambda n: 1 - F(2, n + 1)
assert [a(n) for n in range(4)] == QUOTED["first"]
assert all(a(n) >= QUOTED["delta"] for n in range(QUOTED["N"], 2000))
assert a(2) == QUOTED["a2"] < QUOTED["delta"]
# non-example: for delta = 1/k and N, n = max(N, k) gives 1/(n+1) < delta
for k in range(1, 50):
    for N in range(0, 50):
        n = max(N, k)
        assert n >= N and F(1, n + 1) < F(1, k)
print("ok")
