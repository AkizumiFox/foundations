"""exr-quantifier-rhetoric-b2 (Ch 5, Section 5.2): 4 | 5^n - 1; 5^(n+1) - 1 = 5(5^n - 1) + 4 = 4(5k + 1)."""

QUOTED = {"base_witness": 0, "step_witness": "5k+1"}

for m in range(0, 40):
    assert 5**(m + 1) - 1 == 5 * (5**m - 1) + 4
for k in range(-30, 31):
    assert 5 * 4 * k + 4 == 4 * (5 * k + 1)
assert 5**0 - 1 == 4 * QUOTED["base_witness"]
for m in range(0, 40):
    assert (5**m - 1) % 4 == 0
    kk = (5**m - 1) // 4
    assert 5**(m + 1) - 1 == 4 * (5 * kk + 1)
print("exr-quantifier-rhetoric-b2: all quoted values check")
