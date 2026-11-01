"""exr-finite-sums-b1: (a) sum_{k=1}^{n} 1/((2k-1)(2k+1)) = b_{n+1} - b_1 = (1/2)(1 - 1/(2n+1)) = n/(2n+1); (b) k*k! = (k+1)! - k!, sum = (n+1)! - 1, check n = 2: 1 + 4 = 5 = 6 - 1."""
from fractions import Fraction as Fr
from math import factorial
QUOTED = {"b_check": (1, 4, 5, 6)}
c = lambda k: -Fr(1, 2 * (2 * k - 1))
for n in range(1, 100):
    S = sum(Fr(1, (2 * k - 1) * (2 * k + 1)) for k in range(1, n + 1))
    assert S == c(n + 1) - c(1) == Fr(1, 2) * (1 - Fr(1, 2 * n + 1)) == Fr(n, 2 * n + 1)
    assert sum(k * factorial(k) for k in range(1, n + 1)) == factorial(n + 1) - 1
for k in range(0, 50):
    assert k * factorial(k) == factorial(k + 1) - factorial(k)
    assert factorial(k + 1) == factorial(k) * (k + 1)
t1, t2 = 1 * factorial(1), 2 * factorial(2)
assert (t1, t2, t1 + t2, factorial(3)) == QUOTED["b_check"] and t1 + t2 == factorial(3) - 1
print("ok")
