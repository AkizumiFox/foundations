"""exm-contrapositive-mod-three (F2.2 §04): if 3 does not divide n^2 + n + 1, then n % 3 in {0, 2};
n = 3q + 1 gives n^2 + n + 1 = 9q^2 + 9q + 3; remainders 0 and 2 give n^2 + n + 1 = 1 and 7 at n = 0, 2."""
for q in range(-300, 300):
    n = 3 * q + 1
    assert n * n + n + 1 == 9 * q * q + 9 * q + 3 == 3 * (3 * q * q + 3 * q + 1)
for n in range(-1000, 1000):
    if (n * n + n + 1) % 3 != 0:
        assert n % 3 in (0, 2)
    assert ((n * n + n + 1) % 3 == 0) == (n % 3 == 1)
assert 0 * 0 + 0 + 1 == 1 and 2 * 2 + 2 + 1 == 7
# Quick check (a): x^2 != x => x != 1; (b) no integer square is 2
assert all(n * n != 2 for n in range(-100, 100))
print("exm-contrapositive-mod-three: all quoted values check")
