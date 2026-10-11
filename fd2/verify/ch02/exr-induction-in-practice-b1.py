"""exr-induction-in-practice-b1 (Ch 7, 02): 5 | 6^n - 1, and 6^(n+1) - 1 = 6(6^n - 1) + 5 = 5(6k + 1)."""
for n in range(0, 80):
    assert (6 ** n - 1) % 5 == 0
    k = (6 ** n - 1) // 5
    assert 6 ** (n + 1) - 1 == 6 * (6 ** n - 1) + 5 == 5 * (6 * k + 1)
print("exr-induction-in-practice-b1: all quoted values check")
