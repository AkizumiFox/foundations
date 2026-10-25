"""exm-parity-of-sums (F2.1 §01): (2k+1) + (2l+1) = 2(k + l + 1); 2k + (2l+1) = 2(k + l) + 1; case a = 2 of
exm-divides-combination for both even."""
QUOTED = {"a": 2}
R = range(-30, 31)
for k in R:
    for l in R:
        assert (2 * k + 1) + (2 * l + 1) == 2 * (k + l + 1)
        assert 2 * k + (2 * l + 1) == 2 * (k + l) + 1
        assert (2 * k + 2 * l) % QUOTED["a"] == 0
assert all((m + n) % 2 == (0 if m % 2 == n % 2 else 1) for m in R for n in R)
print("exm-parity-of-sums: all quoted values check")
