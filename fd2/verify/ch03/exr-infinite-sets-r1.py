"""exr-infinite-sets-r1: every n >= 1 is a sum of distinct powers of 2; 13 = 2^3 + 2^2 + 2^0."""
QUOTED = {"13": [3, 2, 0]}


def decompose(n):
    out = []
    while n:
        m = 0
        while 2**m <= n:  # least m with 2^m > n
            m += 1
        K = m - 1
        assert 2**K <= n < 2**(K + 1)
        out.append(K)
        n -= 2**K
        assert n < 2**K
    return out


assert decompose(13) == QUOTED["13"]
for n in range(1, 5000):
    ks = decompose(n)
    assert ks == sorted(set(ks), reverse=True) and sum(2**k for k in ks) == n
    assert 2**n >= 1 + n
print("ok")
