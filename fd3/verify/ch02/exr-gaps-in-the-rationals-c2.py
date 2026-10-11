"""exr-gaps-in-the-rationals-c2: the general descent identity (nq - kp)^2 - n(p - kq)^2 =
(k^2 - n)(p^2 - nq^2); q(nq - kp) = p(p - kq) - (p^2 - nq^2); the general maps' four identities;
the witness n = 5, k = 2, q = 10, p = 28 (nq - kp = -6); k with k^2 <= n < (k+1)^2 from the
least element of T; A_n has a rational sup exactly for perfect squares (sup = k), on n <= 50
(the 'no sup' side is checked via: no rational square root with small denominators)."""
from fractions import Fraction as F
QUOTED = {"witness": (5, 2, 10, 28, -6)}
R = range(-4, 5)
for n in R:
    for k in R:
        for p in R:
            for q in R:
                assert (n*q - k*p)**2 - n*(p - k*q)**2 == (k*k - n)*(p*p - n*q*q)
                assert q*(n*q - k*p) == p*(p - k*q) - (p*p - n*q*q)
n_, k_, q_, p_, d_ = QUOTED["witness"]
assert k_*q_ < p_ < (k_ + 1)*q_ and n_*q_ - k_*p_ == d_
for n in range(1, 30):
    tt = lambda s: (s*s + n) / (2*s)
    uu = lambda s: 2*n*s / (s*s + n)
    for s in [F(a, b) for a in range(1, 25) for b in range(1, 12)]:
        assert tt(s)**2 - n == (s*s - n)**2 / (4*s*s)
        assert s - tt(s) == (s*s - n) / (2*s)
        assert uu(s) - s == s*(n - s*s) / (s*s + n)
        assert n - uu(s)**2 == n*(s*s - n)**2 / (s*s + n)**2
for n in range(1, 51):
    T = [m for m in range(0, n + 2) if n < m*m]
    l = min(T); k = l - 1
    assert n + 1 in T and 0 not in T and k >= 0 and k*k <= n < (k + 1)**2
    square = (k*k == n)
    has_root = any(p*p == n*q*q for q in range(1, 60) for p in range(1, 60*n))
    assert has_root == square
    if not square:
        # descent step on near-solutions keeps q' in (0, q) and p' > 0 when p^2 = n q^2 would hold;
        # here just check the bounds kq < p < (k+1)q imply 0 < p - kq < q
        for q in range(1, 30):
            for p in range(k*q + 1, (k + 1)*q):
                assert 0 < p - k*q < q
print("ok")
