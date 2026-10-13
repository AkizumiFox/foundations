"""exr-writing-proofs-c1 (Ch 5, Section 5.5): f(x) = 2x + 3; f(x) - f(a) = 2(x - a);
delta = eps/2 works for every a."""
from fractions import Fraction as F
QUOTED = {"delta": "eps/2"}
f = lambda x: 2 * x + 3
for eps in [F(1), F(1, 7), F(3, 1000)]:
    d = eps / 2
    assert d > 0
    for a in [F(k, 5) for k in range(-20, 21)]:
        for t in range(-99, 100):
            x = a + d * F(t, 100)          # |x - a| < d
            assert f(x) - f(a) == 2 * (x - a)
            assert abs(f(x) - f(a)) == 2 * abs(x - a) < 2 * d == eps
print("exr-writing-proofs-c1: all quoted values check")
