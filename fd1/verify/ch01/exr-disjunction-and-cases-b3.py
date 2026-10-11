"""exr-disjunction-and-cases-b3 (Ch 1, Section 1.7): (2k)^2 = 4k^2, (2k+1)^2 = 4(k^2+k)+1;
36 = 4*9, 49 = 4*12 + 1."""
QUOTED = {"6^2": (36, 4, 9, 0), "7^2": (49, 4, 12, 1)}

for k in range(-200, 201):
    assert (2 * k) ** 2 == 4 * k * k
    assert (2 * k + 1) ** 2 == 4 * k * k + 4 * k + 1 == 4 * (k * k + k) + 1
for n in range(-500, 501):
    assert n * n % 4 in (0, 1)
for base, (sq, four, qt, rem) in ((6, QUOTED["6^2"]), (7, QUOTED["7^2"])):
    assert base ** 2 == sq == four * qt + rem
print("exr-disjunction-and-cases-b3: all quoted values check")
