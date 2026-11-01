"""exr-convex-sets-and-hulls-r2: f(t) = <(1, t, t^2), (a, b, c)>; and the R1/R3 checks:
R1 unit ball in cube in ball of radius sqrt n (random), R3 |uz - uc| = |z - c| and conj(u) w maps back."""
from fractions import Fraction as F
import random, cmath, math
QUOTED = {"normal": "(1, t, t^2)"}
random.seed(5)
for _ in range(2000):
    a, b, c, t = (F(random.randint(-20, 20), random.randint(1, 9)) for _ in range(4))
    assert a + b * t + c * t**2 == 1 * a + t * b + t**2 * c
for _ in range(2000):
    n = random.randint(1, 5); x = [random.uniform(-1, 1) for _ in range(n)]
    nx = math.sqrt(sum(v * v for v in x))
    assert nx <= math.sqrt(n) + 1e-12
    if nx <= 1: assert all(abs(v) <= 1 for v in x)
    u = cmath.exp(1j * random.uniform(0, 6.3)); z = complex(random.uniform(-3, 3), random.uniform(-3, 3)); cc = complex(random.uniform(-3, 3), random.uniform(-3, 3))
    assert abs(abs(u * z - u * cc) - abs(z - cc)) < 1e-9
    w = complex(random.uniform(-3, 3), random.uniform(-3, 3)); zz = u.conjugate() * w
    assert abs(u * zz - w) < 1e-9 and abs(abs(zz - cc) - abs(w - u * cc)) < 1e-9
print("ok")
