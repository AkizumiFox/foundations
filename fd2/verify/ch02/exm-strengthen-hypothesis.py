"""exm-strengthen-hypothesis: S_n <= 2 - 1/n, the step inequality, and the bad hypothetical."""
from fractions import Fraction as Fr

QUOTED = {"S1": 1}
S = Fr(0)
for n in range(1, 400):
    S += Fr(1, n * n)
    if n == 1:
        assert S == QUOTED["S1"] == 2 - Fr(1, 1)
    assert S <= 2 - Fr(1, n) < 2
    assert Fr(1, (n + 1) ** 2) <= Fr(1, n) - Fr(1, n + 1) == Fr(1, n * (n + 1))
    # a value allowed by "S_n < 2" from which the next sum exceeds 2
    T = 2 - Fr(1, 2 * (n + 1) ** 2)
    assert T < 2 and T + Fr(1, (n + 1) ** 2) > 2
print("ok")
