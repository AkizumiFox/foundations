"""exr-excluded-middle-r4 (Ch 5, Section 5.7): n^3 - n = (n-1)n(n+1), and the three case
factorizations n = 3k: 3(3k-1)k(3k+1); n = 3k+1: 3k(3k+1)(3k+2); n = 3k+2: 3(3k+1)(3k+2)(k+1);
(-m)^3 - (-m) = -(m^3 - m). Each identity is a polynomial identity of degree <= 3 in one
variable, so agreement at more than 4 points proves it; we check many."""

QUOTED = {"divisor": 3}

for n in range(-300, 301):
    assert n ** 3 - n == (n - 1) * n * (n + 1)
    assert (n ** 3 - n) % QUOTED["divisor"] == 0
for k in range(-300, 301):
    n = 3 * k
    assert n ** 3 - n == 3 * ((3 * k - 1) * k * (3 * k + 1))
    n = 3 * k + 1
    assert n ** 3 - n == (3 * k) * (3 * k + 1) * (3 * k + 2) == 3 * (k * (3 * k + 1) * (3 * k + 2))
    n = 3 * k + 2
    assert n ** 3 - n == (3 * k + 1) * (3 * k + 2) * (3 * k + 3) == 3 * ((3 * k + 1) * (3 * k + 2) * (k + 1))
for m in range(1, 300):
    assert (-m) ** 3 - (-m) == -(m ** 3 - m)
print("exr-excluded-middle-r4: all quoted values check")
