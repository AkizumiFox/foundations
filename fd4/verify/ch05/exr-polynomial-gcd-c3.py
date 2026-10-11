"""exr-polynomial-gcd-c3: gcd(x^m - 1, x^n - 1) = x^gcd(m,n) - 1, checked for small m, n."""
import math
from _s0102_poly import gcd_run, xpow, sub, P

QUOTED = {"gcd(12, 18)": 6, "exponents": (12, 18)}
def b(m, p):
    return sub(xpow(m, p), P(1, p=p), p)
for p in (None, 2, 3):
    for m in range(0, 13):
        for n in range(0, 13):
            if m == n == 0:
                continue
            u, v = (b(m, p), b(n, p)) if n else (b(n, p), b(m, p))  # algorithm needs v != 0
            got = gcd_run(u, v, p)[1]
            assert got == b(math.gcd(m, n), p), (p, m, n)
m, n = QUOTED["exponents"]
assert math.gcd(m, n) == QUOTED["gcd(12, 18)"]
assert gcd_run(b(12, None), b(18, None))[1] == b(6, None)
print("ok")
