"""exm-power-inequality (Ch 3, Section 3.2): 3^n >= 2n + 1, and the step's estimates."""
QUOTED = {"base": (0, 1)}

for n in range(0, 300):
    assert 3 ** n >= 2 * n + 1
    assert 3 * (2 * n + 1) == 6 * n + 3 and 6 * n + 3 >= 2 * n + 3 == 2 * (n + 1) + 1
assert 3 ** 0 == 2 * 0 + 1 == 1
print("exm-power-inequality: all quoted values check")
