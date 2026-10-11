"""exr-existential-elimination-b3 (Ch 4, Section 4.6): (2k + 1)(2l + 1) = 2(2kl + k + l) + 1."""
QUOTED = {"lines": 8}
R = range(-60, 61)
assert all((2 * k + 1) * (2 * l + 1) == 4 * k * l + 2 * k + 2 * l + 1
           == 2 * (2 * k * l + k + l) + 1 for k in R for l in R)
print("exr-existential-elimination-b3: all quoted values check")
