"""exr-negation-and-contradiction-b5 (Ch 2, Section 2.2): from sqrt 2 to sqrt p.
(E_p) for p = 2, 3, 5, 7 on a range; (E_6) on |n| <= 2000 (taken as given in the item);
(E_9) fails at n = 3 (9 | 3^2, 9 does not divide 3); (L_6) from (L): a, b not both even are
not both divisible by 6; the algebra a^2 = p b^2, a = pm  =>  b^2 = p m^2; and no a/b with
a^2 = p b^2 for p = 2, 3, 5, 6, 7 in a range, while 3/1 squares to 9."""
QUOTED = {"E9 witness": 3, "primes": (2, 3, 5, 7), "sqrt 9": (3, 1)}

for p in QUOTED["primes"]:
    for n in range(-3000, 3001):
        if (n * n) % p == 0:
            assert n % p == 0
N = 2000  # search range for (E_6), not quoted in the text
for n in range(-N, N + 1):
    if (n * n) % 6 == 0:
        assert n % 6 == 0
w = QUOTED["E9 witness"]
assert (w * w) % 9 == 0 and w % 9 != 0
# (L_6) from (L): if 6 divides both a and b, then both are even
for a in range(-60, 61):
    for b in range(1, 61):
        if a % 6 == 0 and b % 6 == 0:
            assert a % 2 == 0 and b % 2 == 0
# algebra of (a)
for p in (2, 3, 5, 7):
    for m in range(-50, 51):
        for b in range(-50, 51):
            a = p * m
            assert (a * a == p * b * b) == (b * b == p * m * m)
for p in (2, 3, 5, 6, 7):
    for b in range(1, 400):
        for a in range(0, 3 * b):
            assert a * a != p * b * b
a, b = QUOTED["sqrt 9"]
assert a * a == 9 * b * b and (a * a) % 9 == 0 and a % 9 != 0
print("exr-negation-and-contradiction-b5: all quoted values check")
