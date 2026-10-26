"""exm-bisection-square-root-two (Section 5.5): bisection of A = {q in Q : q^2 < 2} from (l_0, u_0) = (0, 2).
Checks: every end >= 0; l_k^2 < 2 <= u_k^2 (so l_k < r <= u_k with r^2 = 2, r > 0); left ends non-decreasing;
the right ends and the Newton sequence x_0 = 2, x_{n+1} = (x_n + 2/x_n)/2 (exm-newton-rationals-sqrt2) get close:
|u_k - x_n| <= 2/2^k + (x_n - sqrt2) bound, checked as |u_k - x_n| < 2/2^k + e_n with e_n = x_n^2 - 2."""
from fractions import Fraction as F
QUOTED = {"l0": 0, "u0": 2, "D": 2}
l, u = F(QUOTED["l0"]), F(QUOTED["u0"])
D = u - l
assert D == QUOTED["D"]
ends = [(l, u)]
for k in range(60):
    c = (l + u) / 2
    l, u = (l, c) if (c > 0 and c * c >= 2) else (c, u)
    ends.append((l, u))
prev_l = F(0)
for k, (l, u) in enumerate(ends):
    assert l >= 0 and u > l and l >= prev_l
    assert l * l < 2 <= u * u and u - l == D / 2 ** k
    prev_l = l
x = F(2)
for n in range(5):
    e = x * x - 2
    assert e > 0
    for k in range(0, 60, 7):
        assert abs(ends[k][1] - x) < D / 2 ** k + e
    x = (x + 2 / x) / 2
print("ok")
