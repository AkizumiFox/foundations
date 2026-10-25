"""exr-contrapositive-and-contradiction-c2 (F2.2 §04): p_1 = 2, p_{n+1} the least prime > p_n;
(a) every prime <= p_n is among p_1..p_n; (b) p_{n+1} <= p_1...p_n + 1; (c) p_n <= 2^(2^(n-1));
the exponent sum 2^0 + ... + 2^(n-1) = 2^n - 1 and 2^(2^n - 1) + 1 <= 2^(2^n);
(d) 3*5 + 1 = 16 = 2^4; 2*7 + 1 = 15 = 3*5, prime factors off the list (checked for n <= 30)."""
QUOTED = {"p2_p3": (3, 5), "lists": (2, 7), "values": (16, 15)}
from math import prod
def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))
N = 30
ps = [2]
while len(ps) < N + 1:
    q = ps[-1] + 1
    while not is_prime(q):
        q += 1
    ps.append(q)
assert ps[:3] == [2, 3, 5]
for n in range(1, N + 1):
    pn = ps[n - 1]
    assert [q for q in range(2, pn + 1) if is_prime(q)] == ps[:n]          # (a)
    assert ps[n] <= prod(ps[:n]) + 1                                       # (b)
    assert pn <= 2 ** (2 ** (n - 1))                                       # (c)
    assert sum(2 ** (k - 1) for k in range(1, n + 1)) == 2 ** n - 1
    assert 2 ** (2 ** n - 1) + 1 <= 2 ** (2 ** n)
assert 3 * 5 + 1 == 16 == 2 ** 4 and 2 * 7 + 1 == 15 == 3 * 5               # (d)
for L in ((3, 5), (2, 7)):
    P = prod(L) + 1
    fs = [d for d in range(2, P + 1) if P % d == 0 and is_prime(d)]
    assert fs and not is_prime(P) and all(d not in L for d in fs)
print("exr-contrapositive-and-contradiction-c2: all quoted values check")
