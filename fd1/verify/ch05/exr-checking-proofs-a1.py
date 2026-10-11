"""exr-checking-proofs-a1 (Ch 5, Section 5.6): 3^n > n^2 for n = 0..4; A = {0, 1}, f(x) = x has a
zero but does not vanish on A; 4 is even and not divisible by 6; x = 0 is neither > 0 nor < 0."""
QUOTED = {"checked": [0, 1, 2, 3, 4]}
assert all(3 ** n > n * n for n in QUOTED["checked"])
A, f = [0, 1], (lambda x: x)
assert any(f(x) == 0 for x in A) and not all(f(x) == 0 for x in A)
assert 4 % 2 == 0 and 4 % 6 != 0
assert not (0 > 0 or 0 < 0)
print("exr-checking-proofs-a1: all quoted values check")
