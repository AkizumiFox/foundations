"""exr-the-least-upper-bound-property-c2: bisection in Q on A = {q : q^2 < 2}, (l_0, u_0) = (0, 2), D = 2;
l_k^2 < 2 <= u_k^2 (indeed > 2), u_k - l_k = D/2^k, l_k non-decreasing, u_k non-increasing;
h = min(1, (2 - u^2)/(2(2u + 1))) gives (u + h)^2 <= u^2 + (2u + 1)h <= u^2 + (2 - u^2)/2 < 2 for 0 <= u, u^2 < 2."""
from fractions import Fraction as F
import random
QUOTED = {"l0": 0, "D": 2}
l, u = F(1) - 1, F(2)
assert l == QUOTED["l0"] and u - l == QUOTED["D"]
D = u - l
for k in range(60):
    assert l * l < 2 < u * u and u - l == D / 2 ** k
    c = (l + u) / 2
    nl, nu = (l, c) if c * c >= 2 else (c, u)
    assert l <= nl and nu <= u
    l, u = nl, nu
random.seed(1)
for _ in range(2000):
    # u rational in [0, sqrt 2)
    u = F(random.randint(0, 10**6), 10**6) * F(141421, 100000)
    if u * u >= 2:
        continue
    h = min(F(1), (2 - u * u) / (2 * (2 * u + 1)))
    assert h > 0
    assert (u + h) ** 2 <= u * u + (2 * u + 1) * h <= u * u + (2 - u * u) / 2 < 2
print("ok")
