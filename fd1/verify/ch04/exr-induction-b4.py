"""exr-induction-b4 (Ch 4, Section 4.2): 6 | n^3 - n; the step identity."""
QUOTED = {"divisor": 6}

for n in range(0, 500):
    assert (n + 1) ** 3 - (n + 1) == n ** 3 + 3 * n * n + 2 * n == (n ** 3 - n) + 3 * n * (n + 1)
    assert (n * (n + 1)) % 2 == 0 and (n ** 3 - n) % 6 == 0
print("exr-induction-b4: all quoted values check")
