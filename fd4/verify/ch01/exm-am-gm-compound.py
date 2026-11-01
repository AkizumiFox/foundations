"""exm-am-gm-compound (03): sum of n copies of 1+1/n and 1 is n+2, mean (n+2)/(n+1) = 1+1/(n+1);
(1+1/n)^n strictly increasing; first terms 2, 9/4, 64/27; bounded by 3 (claimed for 1.5)."""
from fractions import Fraction as Fr
QUOTED = {"first": [Fr(2), Fr(9, 4), Fr(64, 27)]}
e = lambda n: (1 + Fr(1, n)) ** n
assert [e(n) for n in (1, 2, 3)] == QUOTED["first"]
for n in range(1, 80):
    s = n * (1 + Fr(1, n)) + 1
    assert s == n + 2 and s / (n + 1) == 1 + Fr(1, n + 1)
    assert e(n) < e(n + 1) < 3
print("ok")
