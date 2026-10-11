"""exr-frobenius-and-fermat-r3: p.1 = 0 in F_p (so char F_p = p != 0), e.g. p = 2: 1 + 1 = 0;
i^2 = -1 in C."""
QUOTED = {"p_example": 2}
p = QUOTED["p_example"]
assert (1 + 1) % p == 0
for q in (2, 3, 5, 7):
    assert (q * 1) % q == 0
assert complex(0, 1) ** 2 == -1
print("ok")
