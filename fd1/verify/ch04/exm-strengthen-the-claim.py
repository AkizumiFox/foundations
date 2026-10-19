"""exm-strengthen-the-claim (Ch 4, Section 4.2): S_n = n/(n+1) exactly for n <= 200;
S_1, S_2, S_3; the step algebra; the first try fails: a value allowed by "S_n < 1" with S_(n+1) > 1."""
from fractions import Fraction as F

QUOTED = {"S_1": F(1, 2), "S_2": F(2, 3), "S_3": F(3, 4), "S_2 terms": F(1, 6), "S_3 term": F(1, 12)}

S = F(0)
for n in range(1, 201):
    S += F(1, n * (n + 1))
    assert S == F(n, n + 1) and S < 1
    # step algebra: n/(n+1) + 1/((n+1)(n+2)) = (n(n+2)+1)/((n+1)(n+2)) = (n+1)^2/((n+1)(n+2)) = (n+1)/(n+2)
    assert n * (n + 2) + 1 == (n + 1) ** 2
    assert F(n, n + 1) + F(1, (n + 1) * (n + 2)) == F(n + 1, n + 2)
    # first try: a value x < 1 larger than 1 - 1/((n+1)(n+2)) gives x + 1/((n+1)(n+2)) > 1
    t = F(1, (n + 1) * (n + 2))
    x = 1 - t / 2
    assert x < 1 and x > 1 - t and x + t > 1
assert F(1, 2) + F(1, 6) == F(2, 3) and F(2, 3) + F(1, 12) == F(3, 4)
print("exm-strengthen-the-claim: all quoted values check")
