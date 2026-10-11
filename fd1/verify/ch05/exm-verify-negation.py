"""exm-verify-negation (Proof C, Ch 5, Section 5.6): n^2 - 2 is never divisible by 4; the algebra
n^2 = 4k + 2 = 2(2k + 1), 4m^2 = 4k + 2 gives 1 = 2(m^2 - k)."""
QUOTED = {}
for n in range(-5000, 5001):
    assert (n * n - 2) % 4 != 0
for k in range(-200, 201):
    assert 4 * k + 2 == 2 * (2 * k + 1)
    for m in range(-50, 51):
        assert (4 * m * m == 4 * k + 2) == (1 == 2 * (m * m - k))
print("exm-verify-negation: all quoted values check")
