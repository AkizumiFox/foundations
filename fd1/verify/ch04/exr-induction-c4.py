"""exr-induction-c4 (Ch 4, Section 4.2): the false thesis (n^2+n+2)/2; its step is correct;
the true sum is (n^2+n)/2; any constant c passes the step; the base case forces c = 0."""
from fractions import Fraction as F

QUOTED = {"base mismatch": (1, 2), "excess": 1}

for n in range(1, 300):
    assert sum(range(1, n + 1)) == F(n * n + n, 2)
    assert F(n * n + n + 2, 2) - sum(range(1, n + 1)) == 1                        # larger by 1
    assert F(n * n + n + 2, 2) + (n + 1) == F(n * n + 3 * n + 4, 2) == F((n + 1) ** 2 + (n + 1) + 2, 2)
    for c in (F(-3), F(0), F(5, 7), F(10)):
        assert F(n * n + n, 2) + c + (n + 1) == F(n * n + 3 * n + 2, 2) + c == F((n + 1) ** 2 + (n + 1), 2) + c
assert F(1 + 1 + 2, 2) == 2 and F(1 + 1, 2) == 1
print("exr-induction-c4: all quoted values check")
