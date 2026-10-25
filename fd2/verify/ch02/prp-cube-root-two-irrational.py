"""prp-cube-root-two-irrational (F2.2 §04): no p^3 = 2 q^3 with 0 < q <= 10^4;
p^3 even => p even on a range; (2k+1)^3 = 8k^3 + 12k^2 + 6k + 1; 8 s^3 = 2 q^3 => q^3 = 4 s^3;
quick check: p^3 = 3 q^3 with q odd forces p odd."""
def icbrt(m):
    r = round(abs(m) ** (1 / 3))
    for c in (r - 1, r, r + 1):
        if c ** 3 == abs(m):
            return c
    return None
for q in range(1, 10 ** 4 + 1):
    assert icbrt(2 * q ** 3) is None
for p in range(-2000, 2000):
    if p ** 3 % 2 == 0:
        assert p % 2 == 0
for k in range(-200, 200):
    assert (2 * k + 1) ** 3 == 8 * k ** 3 + 12 * k ** 2 + 6 * k + 1 == 2 * (4 * k ** 3 + 6 * k ** 2 + 3 * k) + 1
for s in range(-50, 50):
    assert (2 * s) ** 3 == 8 * s ** 3 and 8 * s ** 3 // 2 == 4 * s ** 3
for q in range(1, 200, 2):
    assert (3 * q ** 3) % 2 == 1
print("prp-cube-root-two-irrational: all quoted values check")
