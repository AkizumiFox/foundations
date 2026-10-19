"""exr-reductio-and-classical-rules-r1 (Ch 2 s05): n^2 != 4n + 2 for |n| <= 10^4; n^2 = 4n + 2 would
make n^2 = 2(2n + 1) even; with n = 2k it gives 2k^2 = 4k + 1, even against odd."""
QUOTED = {"range": 10**4}
N = QUOTED["range"]
for n in range(-N, N + 1):
    assert n * n != 4 * n + 2
    assert 4 * n + 2 == 2 * (2 * n + 1)
for k in range(-1000, 1001):
    assert (2 * k) ** 2 - (4 * (2 * k) + 2) == 2 * (2 * k * k - (4 * k + 1))
    assert (2 * k * k) % 2 == 0 and (4 * k + 1) % 2 == 1
print("exr-reductio-and-classical-rules-r1: ok")
