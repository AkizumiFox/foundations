"""exr-naturals-and-well-ordering-b1 (Ch 7, 01): mn = 1 in N only for m = n = 1; n^2 >= n on N."""
QUOTED = {"solutions": [(1, 1)]}
sols = [(m, n) for m in range(0, 100) for n in range(0, 100) if m * n == 1]
assert sols == QUOTED["solutions"]
assert all(n * n >= n for n in range(0, 10000))
print("exr-naturals-and-well-ordering-b1: all quoted values check")
