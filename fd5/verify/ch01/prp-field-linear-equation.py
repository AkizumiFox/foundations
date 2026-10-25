"""prp-field-linear-equation: for ad - bc = D != 0, x = (ed - bf)/D, y = (af - ce)/D solves
ax + by = e, cx + dy = f; the elimination identities d(ax+by) - b(cx+dy) = Dx and
a(cx+dy) - c(ax+by) = Dy; the expansions a(ed - bf) + b(af - ce) = e(ad - bc) and
c(ed - bf) + d(af - ce) = f(ad - bc). Checked with exact rationals on a grid, and in F_p.
Aftermath: x + y = 1, x + y = 0 inconsistent; x + y = 0, 2x + 2y = 0 has (t, -t)."""
QUOTED = {"x numerator": "ed - bf", "y numerator": "af - ce", "denominator": "ad - bc",
          "inconsistent system": ("x + y = 1", "x + y = 0"),
          "system with solutions (t, -t)": ("x + y = 0", "2x + 2y = 0"),
          "no integer solution": "2x = 1"}
from fractions import Fraction as Fr
from itertools import product
vals = [Fr(v) for v in (-2, -1, 0, 1, 3)] + [Fr(1, 2), Fr(-2, 3)]
count = 0
for a, b, c, d in product(vals, repeat=4):
    D = a * d - b * c
    for e, f in product(vals[:4], repeat=2):
        assert a * (e * d - b * f) + b * (a * f - c * e) == e * D
        assert c * (e * d - b * f) + d * (a * f - c * e) == f * D
        for x, y in product(vals[:3], repeat=2):
            assert d * (a * x + b * y) - b * (c * x + d * y) == D * x
            assert a * (c * x + d * y) - c * (a * x + b * y) == D * y
        if D != 0:
            x, y = (e * d - b * f) / D, (a * f - c * e) / D
            assert a * x + b * y == e and c * x + d * y == f
            count += 1
assert count > 0
for p in [2, 3, 5, 7]:
    for a, b, c, d, e, f in product(range(p), repeat=6):
        D = (a * d - b * c) % p
        if D:
            Di = pow(D, p - 2, p)
            x, y = (e * d - b * f) * Di % p, (a * f - c * e) * Di % p
            assert (a * x + b * y - e) % p == 0 and (c * x + d * y - f) % p == 0
            sols = [(u, v) for u in range(p) for v in range(p)
                    if (a * u + b * v - e) % p == 0 and (c * u + d * v - f) % p == 0]
            assert sols == [(x, y)]
# the two degenerate systems: (1, 1, 1, 1) and (1, 1, 2, 2) have D = 0; (t, -t) solves 2x + 2y = 0
assert 1 * 1 - 1 * 1 == 0 and 1 * 2 - 1 * 2 == 0
for t in vals:
    assert t + (-t) == 0 and 2 * t + 2 * (-t) == 0

# QUOTED: the printed formulas, read as polynomials, are the ones checked above
import re


def expr(text, **env):
    """Evaluate a printed expression such as "ed - bf" or "2x + 2y" (juxtaposition = product)."""
    return eval(re.sub(r"(?<=[0-9a-z])(?=[a-z])", "*", text), {}, env)


for a, b, c, d, e, f in product(vals[:5], repeat=6):
    env = dict(a=a, b=b, c=c, d=d, e=e, f=f)
    D = expr(QUOTED["denominator"], **env)
    assert D == a * d - b * c
    if D != 0:
        x, y = expr(QUOTED["x numerator"], **env) / D, expr(QUOTED["y numerator"], **env) / D
        assert a * x + b * y == e and c * x + d * y == f


def solutions(system, p):
    eqs = [s.split("=") for s in system]
    return [(u, v) for u in range(p) for v in range(p)
            if all((expr(l, x=u, y=v) - expr(r, x=u, y=v)) % p == 0 for l, r in eqs)]


for p in [2, 3, 5, 7]:
    assert solutions(QUOTED["inconsistent system"], p) == []
    assert solutions(QUOTED["system with solutions (t, -t)"], p) == [(t, -t % p) for t in range(p)]
lhs, rhs = QUOTED["no integer solution"].split("=")
assert all(expr(lhs, x=t) != expr(rhs) for t in range(-50, 51))  # 2x is even, 1 is odd
print("ok")
