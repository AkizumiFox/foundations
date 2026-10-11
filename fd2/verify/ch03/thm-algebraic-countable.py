"""thm-algebraic-countable (examples before it): sqrt2 is a root of x^2 - 2, m/n a root of
nx - m, and sqrt2 + sqrt3 a root of x^4 - 10x^2 + 1. Exact arithmetic in Q(sqrt2, sqrt3),
elements a + b*s2 + c*s3 + d*s6 with rational a, b, c, d."""
from fractions import Fraction as Fr

QUOTED = {"poly_sqrt2": (-2, 0, 1), "poly_sum": (1, 0, -10, 0, 1)}


def mul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    # basis 1, s2, s3, s6 with s2^2 = 2, s3^2 = 3, s6^2 = 6, s2 s3 = s6, s2 s6 = 2 s3, s3 s6 = 3 s2
    return (a*e + 2*b*f + 3*c*g + 6*d*h,
            a*f + b*e + 3*c*h + 3*d*g,
            a*g + c*e + 2*b*h + 2*d*f,
            a*h + d*e + b*g + c*f)


def ev(coeffs, x):
    acc, p = (0, 0, 0, 0), (1, 0, 0, 0)
    for ck in coeffs:  # coeffs c_0, c_1, ...
        acc = tuple(u + ck * v for u, v in zip(acc, p))
        p = mul(p, x)
    return acc


assert ev(QUOTED["poly_sqrt2"], (0, 1, 0, 0)) == (0, 0, 0, 0)
assert ev(QUOTED["poly_sum"], (0, 1, 1, 0)) == (0, 0, 0, 0)
for m in range(-7, 8):
    for n in range(1, 8):
        x = Fr(m, n)
        assert n * x - m == 0          # c = (-m, n)
print("thm-algebraic-countable: all quoted values check")
