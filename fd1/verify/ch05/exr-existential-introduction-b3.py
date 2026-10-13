"""exr-existential-introduction-b3 (Ch 4, Section 4.5): n * n = n + 2 over Z, witness 2
(and -1); phi marks three of the four 2's of 2 * 2 = 2 + 2."""
from _s0102_fol import V, C, F, Eq, sub, free_for

QUOTED = {"witness": 2, "other witness": -1, "marked 2's": 3}

n, two = V('n'), C('2')
line = Eq(F('*', two, two), F('+', two, two))
phi = Eq(F('*', n, n), F('+', n, two))
assert sub(phi, two, 'n') == line and free_for(two, 'n', phi)
# marking all four gives a different statement
phi4 = Eq(F('*', n, n), F('+', n, n))
assert sub(phi4, two, 'n') == line and phi4 != phi
# count: phi has three occurrences of n
assert str(phi).count("'n'") == QUOTED["marked 2's"]
w, v = QUOTED["witness"], QUOTED["other witness"]
assert w * w == w + 2 == 4 and v * v == v + 2 == 1
assert sorted(k for k in range(-100, 101) if k * k == k + 2) == [-1, 2]
print("exr-existential-introduction-b3: all quoted values check")
