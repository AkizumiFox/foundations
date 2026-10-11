"""exr-induction-a1 (Ch 3, Section 3.2): 3 | 4^n - 1 (base 4^0 - 1 = 0); n >= 12 is 4a + 5b; base cases 12-15."""
QUOTED = {"base (i)": (0, 3), "bound (ii)": 12, "base cases (ii)": (12, 13, 14, 15)}

for n in range(0, 200):
    assert (4 ** n - 1) % 3 == 0 and 4 ** (n + 1) - 1 == 4 * (4 ** n - 1) + 3


def rep(n):
    return any((n - 5 * b) >= 0 and (n - 5 * b) % 4 == 0 for b in range(n // 5 + 1))


assert all(rep(n) for n in range(12, 1000)) and not rep(11)
assert 12 == 4 * 3 and 13 == 4 * 2 + 5 and 14 == 4 + 5 * 2 and 15 == 5 * 3
print("exr-induction-a1: all quoted values check")
