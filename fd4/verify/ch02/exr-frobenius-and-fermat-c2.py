"""exr-frobenius-and-fermat-c2: induction (r.1)^p = r.1 in F_p for r < 3p; for p = 2, -1 = 1;
for odd p, (-1)^p = -1; [a]^p = [a] for negative a."""
QUOTED = {"p_special": 2}
assert (-1) % QUOTED["p_special"] == 1 % QUOTED["p_special"]
for p in (2, 3, 5, 7, 11, 13):
    for r in range(3 * p):
        assert pow(r % p, p, p) == r % p
    if p % 2:
        assert (-1) ** p == -1
    for a in range(-40, 0):
        assert pow(a % p, p, p) == a % p
print("ok")
