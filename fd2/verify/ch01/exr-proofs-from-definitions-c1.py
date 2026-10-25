"""exr-proofs-from-definitions-c1 (F2.1 §01): the three forms mod 3, the negatives,
the squares, and (c) 3 | a^2 + b^2 => 3 | a and 3 | b."""
QUOTED = {"sq1": "3(3k^2 + 2k) + 1", "sq2": "3(3k^2 + 4k + 1) + 1"}
# polynomial identities of degree <= 2 in k, checked at 41 points
for k in range(-20, 21):
    assert -(3 * k) == 3 * (-k) and -(3 * k + 1) == 3 * (-k - 1) + 2 and -(3 * k + 2) == 3 * (-k - 1) + 1
    assert (3 * k)**2 == 3 * (3 * k**2)
    assert (3 * k + 1)**2 == 9 * k**2 + 6 * k + 1 == 3 * (3 * k**2 + 2 * k) + 1
    assert (3 * k + 2)**2 == 9 * k**2 + 12 * k + 4 == 3 * (3 * k**2 + 4 * k + 1) + 1
# no integer has two forms: 3c in {1, 2} has no integer solution
assert not any(3 * c in (1, 2) for c in range(-100, 101))
assert all((n * n) % 3 == (0 if n % 3 == 0 else 1) for n in range(-90, 91))
R = range(-40, 41)
assert all(a % 3 == 0 and b % 3 == 0 for a in R for b in R if (a * a + b * b) % 3 == 0)
# the two cases of (c): 1 + 0 and 1 + 1 are not 0 mod 3
assert (1 + 0) % 3 == 1 and (1 + 1) % 3 == 2
print("exr-proofs-from-definitions-c1: all quoted values check")
