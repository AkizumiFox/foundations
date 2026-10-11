"""exr-disjunction-and-cases-a1 (Ch 1, Section 1.7): (c) the one-case "proof" that n^2 is even fails at n = 1;
(d) instance P: x > 1, Q: x < 1, R: x > 0 refuted at x = -1; the quick check on x^2 >= 0 splits."""
QUOTED = {"(c) witness": 1, "(d) witness": -1}

n = QUOTED["(c) witness"]
assert n % 2 == 1 and (n * n) % 2 == 1  # n odd (the missing case) and n^2 odd
x = QUOTED["(d) witness"]
P, Q, R = x > 1, x < 1, x > 0
assert (P or Q) and ((not P) or R) and not R
# quick check: split (ii) x > 0 / x < 0 misses 0; (i) and (iii) cover a grid, (iii) overlaps at 0
pts = [k / 4 for k in range(-40, 41)]
assert all(t >= 0 or t < 0 for t in pts)
assert not (0 > 0 or 0 < 0)
assert all(t >= 0 or t <= 0 for t in pts) and (0 >= 0 and 0 <= 0)
assert all(t * t >= 0 for t in pts)
print("exr-disjunction-and-cases-a1: all quoted values check")
