"""exr-equivalence-relations-b4 and the Quick check after exm-method-well-definedness.
Representatives in a window; exact Fractions for the reals-mod-integers part (c)."""
from fractions import Fraction as F

QUOTED = {"qc_bad_pair": (0, 6), "c_diff_num": 16, "c_den": 9, "e_pair": ((1, 2), (2, 4))}

W = range(-30, 31)
def wd(m_in, m_out, g):
    return all((g(a) - g(b)) % m_out == 0 for a in W for b in W if (a - b) % m_in == 0)

# Quick check: (a) Z/6 -> Z, [a] -> a^2 fails at 0, 6; (b) Z/6 -> Z/3, [a]_6 -> [a^2]_3 is well defined
assert (6 - 0) % 6 == 0 and 0 ** 2 == 0 and 6 ** 2 == 36 and 0 != 36
assert wd(6, 3, lambda a: a * a)
for a in W:
    for b in W:
        if (a - b) % 6 == 0:
            k = (a - b) // 6
            assert a * a - b * b == 3 * (2 * k * (a + b))

# (a) ([a],[b]) -> [a - 2b] on Z/6
for a in W:
    for a2 in W:
        if (a - a2) % 6: continue
        for b in range(-12, 13):
            for b2 in range(-12, 13):
                if (b - b2) % 6: continue
                k, l = (a - a2) // 6, (b - b2) // 6
                assert (a - 2 * b) - (a2 - 2 * b2) == 6 * (k - 2 * l)
# (b) [a]_4 -> [2a]_8 well defined; B3 (b) contrast fails
assert wd(4, 8, lambda a: 2 * a)
assert not wd(5, 10, lambda a: a)
# (c) [1/3] = [4/3], squares differ by 5/3, not an integer
x, y = F(1, 3), F(4, 3)
assert (y - x) == 1
d = y * y - x * x
assert d == F(QUOTED["c_diff_num"] - 1, QUOTED["c_den"]) == F(5, 3) and d.denominator != 1 and 0 < d - 1 == F(2, 3) < 1
assert y * y == F(16, 9) and x * x == F(1, 9)
# (d) (a,b) ~ (c,d) iff ad = bc on Z x Z_{>0}; [(a,b)] -> [(a+b, b)] well defined
P = [(a, b) for a in range(-8, 9) for b in range(1, 9)]
rel = lambda p, q: p[0] * q[1] == p[1] * q[0]
assert all(rel((a + b, b), (c + d_, d_)) for (a, b) in P for (c, d_) in P if rel((a, b), (c, d_)))
# (e) [(a,b)] -> [(a+1, b+1)] fails at (1,2) ~ (2,4)
assert rel((1, 2), (2, 4)) and not rel((2, 3), (3, 5)) and 2 * 5 == 10 and 3 * 3 == 9
print("exr-equivalence-relations-b4: all quoted values check")
