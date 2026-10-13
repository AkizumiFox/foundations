"""exm-sum-of-evens (Ch 4, Section 4.6): n = 2k0, m = 2l0 give n + m = 2(k0 + l0)."""
QUOTED = {"lines": 8}
R = range(-60, 61)
assert all(2 * k + 2 * l == 2 * (k + l) for k in R for l in R)
print("exm-sum-of-evens: all quoted values check")
