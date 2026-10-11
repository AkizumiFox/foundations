"""prp-cof-sqrt2-field-archimedean: (a + b r)(c + d r) = (ac + 2bd) + (ad + bc) r and
(a + b r)^{-1} = a/(a^2 - 2b^2) - b/(a^2 - 2b^2) r, computed in Q[r]/(r^2 - 2) with exact pairs;
exm-cof-sqrt2-conjugation: sigma(a + b r) = a - b r respects products."""
from fractions import Fraction as F
import random
QUOTED = {"product": "(ac + 2bd) + (ad + bc)"}
def mul(u, v):
    (a, b), (c, d) = u, v
    return (a * c + 2 * b * d, a * d + b * c)
def inv(u):
    a, b = u; n = a * a - 2 * b * b
    assert n != 0
    return (a / n, -b / n)
def conj(u): return (u[0], -u[1])
random.seed(3)
for _ in range(3000):
    u = (F(random.randint(-20, 20), random.randint(1, 9)), F(random.randint(-20, 20), random.randint(1, 9)))
    v = (F(random.randint(-20, 20), random.randint(1, 9)), F(random.randint(-20, 20), random.randint(1, 9)))
    assert conj(mul(u, v)) == mul(conj(u), conj(v))
    if u != (0, 0):
        assert mul(u, inv(u)) == (1, 0)
        assert mul(u, conj(u)) == (u[0] ** 2 - 2 * u[1] ** 2, 0)
# square of a + b r: (a^2 + 2 b^2) + 2ab r
for a in range(-5, 6):
    for b in range(-5, 6):
        assert mul((a, b), (a, b)) == (a * a + 2 * b * b, 2 * a * b)
print("ok")
