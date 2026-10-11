"""exr-cauchy-sequences-a1 (d): a_n = 1/(n+1) - 1 in Q, eps = 1/2: |a_n| >= 1/2 for n >= 1, a_0 = 0;
least N_0 for tolerance 1/4 is 3 (pair (2, 11) gives exactly 1/4); n_0 = 3, a_3 = -3/4;
a_n < a_3 + 1/4 = -1/2 <= -1/4 for n >= 3."""
from fractions import Fraction as F
QUOTED = {"N0": 3, "a3": F(-3, 4), "c": F(1, 4), "pair": (2, 11)}
a = lambda n: F(1, n + 1) - 1
assert a(0) == 0 and all(abs(a(n)) >= F(1, 2) for n in range(1, 500))
# for m, n >= N0 the differences stay below 1/(N0+1) and approach it; tolerance 1/4 needs 1/(N0+1) <= 1/4
assert F(1, 3 + 1) <= F(1, 4) and not F(1, 2 + 1) <= F(1, 4)
m, n = QUOTED["pair"]
assert abs(a(m) - a(n)) == F(1, 4)
for m in range(3, 200):
    for n in range(3, 200):
        assert abs(a(m) - a(n)) < F(1, 4)
assert a(3) == QUOTED["a3"] and abs(a(3)) >= F(1, 2)
assert a(3) + F(1, 4) == F(-1, 2)
assert all(a(n) <= -QUOTED["c"] for n in range(3, 500))
print("ok")
