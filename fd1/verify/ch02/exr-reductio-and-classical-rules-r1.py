"""exr-reductio-and-classical-rules-r1 (Ch 2 s05): n^2 + 3n is even, by cases on the parity of n:
n = 2k gives 2(2k^2 + 3k), n = 2k + 1 gives (4k^2 + 4k + 1) + (6k + 3) = 2(2k^2 + 5k + 2)."""
QUOTED = {"range": 10**4}
N = QUOTED["range"]
for n in range(-N, N + 1):
    assert (n * n + 3 * n) % 2 == 0
for k in range(-1000, 1001):
    n = 2 * k
    assert n * n + 3 * n == 4 * k * k + 6 * k == 2 * (2 * k * k + 3 * k)
    n = 2 * k + 1
    assert n * n + 3 * n == (4 * k * k + 4 * k + 1) + (6 * k + 3) == 2 * (2 * k * k + 5 * k + 2)
print("exr-reductio-and-classical-rules-r1: ok")
