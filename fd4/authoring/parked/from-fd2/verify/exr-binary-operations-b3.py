"""exr-binary-operations-b3: inverse of x^3 + 1 under composition is cbrt(x - 1);
under pointwise + it is -x^3 - 1; x^2 not injective; also the quick check 2x + 1."""
from fractions import Fraction as F
QUOTED = {"g_witness": 1, "g_zero": 0}


def cbrt(t):
    r = abs(t) ** (1.0 / 3)
    return r if t >= 0 else -r

f = lambda x: x ** 3 + 1
h = lambda x: cbrt(x - 1)
for x in [-3.5, -1, 0, 0.25, 1, 2, 9]:
    assert abs(f(h(x)) - x) < 1e-9 and abs(h(f(x)) - x) < 1e-9
    assert f(x) + (-x ** 3 - 1) == 0
assert 1 ** 2 == (-1) ** 2
g = lambda x: 2 * x + 1
gi = lambda x: (x - 1) / F(2)
for x in [F(-3), F(0), F(5, 7), F(4)]:
    assert g(gi(x)) == x == gi(g(x)) and g(x) + (-2 * x - 1) == 0
assert (QUOTED["g_witness"]) ** 2 == (-QUOTED["g_witness"]) ** 2 and QUOTED["g_zero"] ** 2 == 0
print("exr-binary-operations-b3: all quoted values check")
