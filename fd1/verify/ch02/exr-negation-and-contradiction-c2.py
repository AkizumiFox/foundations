"""exr-negation-and-contradiction-c2 (Ch 2, Section 2.2): the false lemma 4 | n^2 => 4 | n fails
at n = 2; 2 = 2/1 squares to 4; the counterexamples are n = 2 mod 4."""
QUOTED = {"witness n": 2, "2^2": 4}

n = QUOTED["witness n"]
assert n * n == QUOTED["2^2"] and (n * n) % 4 == 0 and n % 4 != 0
bad = [k for k in range(-50, 51) if (k * k) % 4 == 0 and k % 4 != 0]
assert bad and all(k % 4 == 2 for k in bad)
print("exr-negation-and-contradiction-c2: all quoted values check")
