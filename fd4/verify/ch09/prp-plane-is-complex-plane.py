"""prp-plane-is-complex-plane: (t,0)(a,b) = (ta,tb); (-1)w is the complex negative; z conj(w) = (ac + bd, bc - ad), so <z,w> = Re(z conj w)
= Re(conj z w); ||z||^2 = |z|^2 = a^2 + b^2. Exact rational random checks."""
QUOTED = {"product": "(ac + bd, \\; bc - ad)"}
from fractions import Fraction as Fr
import random

def mul(z, w): return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])
def conj(z): return (z[0], -z[1])
random.seed(4)
for _ in range(3000):
    a, b, c, d, t = (Fr(random.randint(-30, 30), random.randint(1, 9)) for _ in range(5))
    z, w = (a, b), (c, d)
    assert mul((t, 0), z) == (t * a, t * b)
    neg = mul((-1, 0), w); assert neg == (-c, -d) and (c + neg[0], d + neg[1]) == (0, 0)
    assert mul(z, conj(w)) == (a * c + b * d, b * c - a * d)
    assert mul(z, conj(w))[0] == a * c + b * d == mul(conj(z), w)[0]
    assert mul(z, conj(z)) == (a * a + b * b, 0)
print("ok")
