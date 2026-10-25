"""exm-three-power-factor (F2.2 §04): every positive n is 3^a * b with 3 not dividing b;
54 = 3^3 * 2, 45 = 3^2 * 5; m = 3m' gives 1 <= m' < m."""
def split(n):
    a = 0
    while n % 3 == 0:
        n //= 3; a += 1
    return a, n
for n in range(1, 20000):
    a, b = split(n)
    assert 3 ** a * b == n and b % 3 != 0
    if n % 3 == 0:
        assert 1 <= n // 3 < n
assert split(54) == (3, 2) and split(45) == (2, 5)
print("exm-three-power-factor: all quoted values check")
