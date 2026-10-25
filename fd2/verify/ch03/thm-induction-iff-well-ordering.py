"""thm-induction-iff-well-ordering (Ch 7, 01): the three witnesses, checked on finite segments.
W1 = N u (N + 1/2): contains 0, closed under +1, predecessor fails at 1/2 (1/2 - 1 = -1/2 not in W1);
     least element of W1 \\ N is 1/2; 1/2 not in N.
W2 = {-n : n in N}: contains 0, predecessor property, 1 not in W2, no least element ((-(n+1)) < -n).
W3 = {k + 1/2 : k in Z}: closed, predecessor property, 0 not in W3, no least element."""
from fractions import Fraction as F

H = F(1, 2)
K = 60
QUOTED = {"m": H, "m_minus_1": -H}

def in_W1(x):
    return x >= 0 and (x.denominator == 1 or x.denominator == 2)

def in_W2(x):
    return x.denominator == 1 and x <= 0

def in_W3(x):
    return x.denominator == 2

seg1 = [F(n) for n in range(K)] + [n + H for n in range(K)]
assert in_W1(F(0)) and all(in_W1(x + 1) for x in seg1)
assert in_W1(QUOTED["m"]) and QUOTED["m"] != 0 and not in_W1(QUOTED["m"] - 1)
assert QUOTED["m"] - 1 == QUOTED["m_minus_1"]
assert min(x for x in seg1 if x.denominator != 1) == QUOTED["m"]
# predecessor fails only at the halves: n + 1/2 with n = 0
assert [x for x in seg1 if x != 0 and not in_W1(x - 1)] == [H]

seg2 = [F(-n) for n in range(K)]
assert in_W2(F(0)) and all(in_W2(x - 1) for x in seg2 if x != 0)
assert not in_W2(F(1))
assert all(F(-(n + 1)) < F(-n) for n in range(K))

seg3 = [k + H for k in range(-K, K)]
assert not in_W3(F(0))
assert all(in_W3(x + 1) and in_W3(x - 1) for x in seg3)
print("thm-induction-iff-well-ordering: all quoted values check")
