"""exr-units-and-crt-b2: (xs + mt)(xs' + nt') = x(xss' + snt' + s'mt) + mn tt' (on a grid of degree-exceeding size in each variable);
(a) unit mod mn iff unit mod m and mod n, all m, n <= 15; m = n = 2: [1]_4, [3]_4 -> ([1],[1])."""
from math import gcd
from itertools import product
for x, s, s2, m, n, t, t2 in product(range(-2, 3), repeat=7):
    assert (x*s + m*t)*(x*s2 + n*t2) == x*(x*s*s2 + s*n*t2 + s2*m*t) + m*n*t*t2
for M in range(1, 16):
    for N in range(1, 16):
        for X in range(-30, 31):
            assert (gcd(X, M * N) == 1) == (gcd(X, M) == 1 and gcd(X, N) == 1)
assert [a for a in range(4) if gcd(a, 4) == 1] == [1, 3] and (1 % 2, 3 % 2) == (1, 1)
print("ok")
