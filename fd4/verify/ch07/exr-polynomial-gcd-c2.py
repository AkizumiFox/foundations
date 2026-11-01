"""exr-polynomial-gcd-c2: gcd(hf, hg) = h gcd(f, g) for monic h; the counterexample without monic."""
from _s0102_poly import P, gcd_run, mul

QUOTED = {"gcd(2x, 2)": 1}
assert gcd_run(P(2, 0), P(2))[1] == P(QUOTED["gcd(2x, 2)"])
assert mul(P(2), gcd_run(P(1, 0), P(1))[1]) == P(2)
cases = [(P(1, 0, -1), P(1, 1, -2), P(1, 3)), (P(1, 0, 0, 0), P(1, 0, 1), P(1, 0, 0, 5)),
         (P(2, 4), P(3, 0, 6), P(1, -1, 1))]
for f, g, h in cases:
    assert gcd_run(mul(h, f), mul(h, g))[1] == mul(h, gcd_run(f, g)[1])
print("ok")
