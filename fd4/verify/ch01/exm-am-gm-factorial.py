"""exm-am-gm-factorial (03): n! <= ((n+1)/2)^n, equality only at n = 1; n = 2: 2 < 9/4;
the remark (n+1)/(2n) <= 3/4 for n >= 2."""
from fractions import Fraction as Fr
from math import factorial
QUOTED = {"n2": (2, Fr(9, 4))}
for n in range(1, 60):
    assert sum(range(1, n + 1)) == n * (n + 1) // 2
    b = Fr(n + 1, 2) ** n
    if n == 1:
        assert factorial(n) == b == 1
    else:
        assert factorial(n) < b
        assert Fr(n + 1, 2 * n) <= Fr(3, 4)
        assert b <= Fr(3, 4) ** n * n ** n
assert factorial(2) == QUOTED["n2"][0] and Fr(3, 2) ** 2 == QUOTED["n2"][1]
print("ok")
