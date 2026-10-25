"""exr-induction-in-practice-b1 (F2.2, 02): 3 | n^3 + 2n, and (n + 1)^3 + 2(n + 1) = (n^3 + 2n) + 3(n^2 + n + 1)."""
for n in range(0, 500):
    assert (n ** 3 + 2 * n) % 3 == 0
    k = (n ** 3 + 2 * n) // 3
    assert (n + 1) ** 3 + 2 * (n + 1) == (n ** 3 + 2 * n) + 3 * (n * n + n + 1) == 3 * (k + n * n + n + 1)
print("exr-induction-in-practice-b1: all quoted values check")
