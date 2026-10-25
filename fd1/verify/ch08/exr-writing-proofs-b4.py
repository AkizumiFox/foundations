"""exr-writing-proofs-b4 (Section 8.5): 7^3 - 7 = 336 = 6*56 = 6*7*8; n^3 - n = (n - 1)n(n + 1);
6 | n^3 - n for |n| <= 500; if m = 2a = 3b then b = 2(a - b) and m = 6(a - b)."""
QUOTED = {"value": 336, "P1": 56, "P2": (6, 7, 8)}
assert 7 ** 3 - 7 == QUOTED["value"] == 6 * QUOTED["P1"]
x, y, z = QUOTED["P2"]
assert x * y * z == 336 and (y, z) == (7, 8) and x == 7 - 1
for n in range(-500, 501):
    assert n ** 3 - n == (n - 1) * n * (n + 1)
    assert (n ** 3 - n) % 6 == 0
    assert (n % 2 == 1) <= ((n - 1) % 2 == 0)
for m in range(-600, 601, 6):
    a, b = m // 2, m // 3
    assert m == 2 * a == 3 * b and b == 2 * (a - b) and m == 6 * (a - b)
print("exr-writing-proofs-b4: all quoted values check")
