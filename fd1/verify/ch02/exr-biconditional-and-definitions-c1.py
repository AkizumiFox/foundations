"""exr-biconditional-and-definitions-c1 (Ch 2, Section 2.4): 6 | n, (2 | n and 3 | n), 6 | n^2
agree; 36k^2 = 6(6k^2); b = 2c+1 gives 3b = 6c + 3 = 2(3c+1)+1."""
QUOTED = {}

for n in range(-3000, 3001):
    i = n % 6 == 0
    ii = n % 2 == 0 and n % 3 == 0
    iii = (n * n) % 6 == 0
    assert i == ii == iii
for k in range(-300, 301):
    assert (6 * k) ** 2 == 36 * k * k == 6 * (6 * k * k)
    assert 3 * (2 * k + 1) == 6 * k + 3 == 2 * (3 * k + 1) + 1
print("exr-biconditional-and-definitions-c1: all quoted values check")
