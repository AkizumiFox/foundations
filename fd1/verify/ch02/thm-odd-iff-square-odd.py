"""thm-odd-iff-square-odd (Ch 2, Section 2.4): n odd iff n^2 odd; n = 2k gives n^2 = 2(2k^2)."""
QUOTED = {}

for n in range(-2000, 2001):
    assert (n % 2 == 1) == ((n * n) % 2 == 1)
for k in range(-500, 501):
    assert (2 * k) ** 2 == 2 * (2 * k * k)
print("thm-odd-iff-square-odd: all quoted values check")
