"""exr-universal-elimination-a1 (Ch 4, Section 4.3): the readings in the solution to (b)."""
QUOTED = {"(ii) x names": -1, "(iii) c": 0, "(iii) a": 1}

# (i) over Z: exists y (y > x) holds for every x (y = x + 1); y > y never holds.
assert all(n + 1 > n for n in range(-500, 500))
assert not any(n > n for n in range(-500, 500))
# (ii) x * x >= 0 for all reals sampled; 3 * x >= 0 fails at x = -1.
assert all(t * t >= 0 for t in [k / 7 for k in range(-100, 100)])
assert not (3 * QUOTED["(ii) x names"] >= 0)
# (iii) over N with P(x) := x >= 1: forall x P(x) is false (0), so line 1 is true;
# line 2: P(1) -> P(0) is 1 >= 1 -> 0 >= 1, which is false.
assert not all(n >= 1 for n in range(0, 100))
a, c = QUOTED["(iii) a"], QUOTED["(iii) c"]
assert (a >= 1) and not (c >= 1)
print("exr-universal-elimination-a1: all quoted values check")
