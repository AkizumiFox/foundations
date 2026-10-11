"""exr-cauchy-sequences-b3: a_n = 2 - 1/(n+1) >= 1; least N_0 for tolerance 1/2 is 1
(pair (0, 1) gives exactly 1/2); n_0 = 1, a_1 = 3/2; a_n > 3/2 - 1/2 = 1 >= 1/2 for n >= 1."""
from fractions import Fraction as F
QUOTED = {"N0": 1, "a1": F(3, 2), "c_proof": F(1, 2), "N_proof": 1, "c_direct": 1, "N_direct": 0}
a = lambda n: 2 - F(1, n + 1)
assert all(a(n) >= QUOTED["c_direct"] for n in range(500))
assert abs(a(0) - a(1)) == F(1, 2)
for m in range(1, 200):
    for n in range(1, 200):
        assert abs(a(m) - a(n)) < F(1, 2)
assert a(1) == QUOTED["a1"] and a(1) - F(1, 2) == 1
assert all(a(n) > 1 for n in range(1, 500))
print("ok")
