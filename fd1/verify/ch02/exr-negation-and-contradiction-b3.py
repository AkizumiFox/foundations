"""exr-negation-and-contradiction-b3 (Ch 2, Section 2.2): (3k+1)^2 = 3(3k^2+2k)+1,
(3k+2)^2 = 3(3k^2+4k+1)+1; 3 | n^2 => 3 | n; p = 3m, p^2 = 3q^2 => q^2 = 3m^2; no p^2 = 3q^2."""
QUOTED = {"(3k+1)^2": (9, 6, 1), "(3k+2)^2": (9, 12, 4)}

for k in range(-300, 301):
    assert (3 * k + 1) ** 2 == 9 * k * k + 6 * k + 1 == 3 * (3 * k * k + 2 * k) + 1
    assert (3 * k + 2) ** 2 == 9 * k * k + 12 * k + 4 == 3 * (3 * k * k + 4 * k + 1) + 1
for n in range(-1000, 1001):
    if (n * n) % 3 == 0:
        assert n % 3 == 0
for m in range(-100, 101):
    for q in range(-100, 101):
        assert ((3 * m) ** 2 == 3 * q * q) == (q * q == 3 * m * m)
for q in range(1, 1500):
    for p in range(0, 2 * q + 1):
        assert p * p != 3 * q * q
for key, (a, b, c) in QUOTED.items():
    shift = 1 if key == "(3k+1)^2" else 2
    assert all((3 * k + shift) ** 2 == a * k * k + b * k + c for k in range(-5, 6))
print("exr-negation-and-contradiction-b3: all quoted values check")
