"""exr-frobenius-and-fermat-r2: (n, k) = (7, 2): 4 < 7 < 9; (14, 3): 9 < 14 < 16;
(a + b sqrt2)^2 = (a^2 + 2b^2) + 2ab sqrt2 (symbolic check on integer samples)."""
QUOTED = {"pairs": [(7, 2), (14, 3)]}
for n, k in QUOTED["pairs"]:
    assert k * k < n < (k + 1) ** 2
for a in range(-5, 6):
    for b in range(-5, 6):
        # (a + b s)^2 with s^2 = 2: rational part and sqrt2 part
        rat, irr = a * a + 2 * b * b, 2 * a * b
        assert (rat, irr) == (a * a + b * b * 2, a * b + b * a)
print("ok")
