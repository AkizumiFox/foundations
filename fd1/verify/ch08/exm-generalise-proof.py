"""exm-generalise-proof (Section 8.5): 18 = 3*6; 17 = 3*5 + 2 and 17 + 1 = 3*6; for every integer
n, one of n, n + 1, n + 2 is a multiple of 3, by the three cases n = 3k, 3k + 1, 3k + 2
(with n + 2 = 3(k + 1), n + 1 = 3(k + 1)); (P2) is the case n = 3k + 2 with k = 5.
The Quick check: 7^2 - 1 = 48 = 8*6; (2k + 1)^2 - 1 = 4k(k + 1); 8 | n^2 - 1 for odd n."""
QUOTED = {"P1": (18, 6), "P2": (17, 5, 2), "check": (48, 6)}
assert 18 == 3 * QUOTED["P1"][1]
assert 17 == 3 * QUOTED["P2"][1] + QUOTED["P2"][2] and 17 + 1 == 3 * 6
assert 17 == 3 * 5 + 2                       # k = 5, third case
for n in range(-300, 301):
    assert any(m % 3 == 0 for m in (n, n + 1, n + 2))
    k, r = divmod(n, 3)
    assert n == 3 * k + r and r in (0, 1, 2)
    if r == 1:
        assert n + 2 == 3 * (k + 1)
    if r == 2:
        assert n + 1 == 3 * (k + 1)
assert 7 ** 2 - 1 == QUOTED["check"][0] == 8 * QUOTED["check"][1]
for k in range(-200, 201):
    n = 2 * k + 1
    assert n * n - 1 == 4 * k * (k + 1) and (k * (k + 1)) % 2 == 0
for n in range(-301, 302, 2):
    assert (n * n - 1) % 8 == 0
print("exm-generalise-proof: all quoted values check")
