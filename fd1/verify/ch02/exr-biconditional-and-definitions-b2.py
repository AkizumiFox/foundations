"""exr-biconditional-and-definitions-b2 (Ch 2, Section 2.4): n even iff n + 3 odd;
2k + 3 = 2(k+1) + 1; 2j + 1 - 3 = 2(j - 1)."""
QUOTED = {}

for n in range(-1000, 1001):
    assert (n % 2 == 0) == ((n + 3) % 2 == 1)
for k in range(-300, 301):
    assert 2 * k + 3 == 2 * (k + 1) + 1 and (2 * k + 1) - 3 == 2 * (k - 1)
print("exr-biconditional-and-definitions-b2: all quoted values check")
