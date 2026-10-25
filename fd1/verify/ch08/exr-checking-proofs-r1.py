"""exr-checking-proofs-r1 (Section 8.6): 9 + 3 = 12, 16 + 4 = 20; n^2 + n = n(n + 1) even for
|n| <= 500; n = 2k gives n(n + 1) = 2(k(n + 1)); n = 2k + 1 gives n + 1 = 2(k + 1) and
n(n + 1) = 2(n(k + 1))."""
QUOTED = {"instances": {3: 12, 4: 20}}
for n, v in QUOTED["instances"].items():
    assert n * n + n == v and v % 2 == 0
for n in range(-500, 501):
    assert n * n + n == n * (n + 1) and (n * n + n) % 2 == 0
    k = n // 2
    if n % 2 == 0:
        assert n * (n + 1) == 2 * (k * (n + 1))
    else:
        assert n == 2 * k + 1 and n + 1 == 2 * (k + 1) and n * (n + 1) == 2 * (n * (k + 1))
print("exr-checking-proofs-r1: all quoted values check")
