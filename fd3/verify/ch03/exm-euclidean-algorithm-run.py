"""exm-euclidean-algorithm-run, the warning after it, and the Quick check after the warning."""
import math

def chain(a, b):
    rows = []
    x, y = a, b
    while y > 0:
        q = (x - (x % y)) // y
        r = x % y  # Python: 0 <= r < y for y > 0
        assert x == q * y + r and 0 <= r < y
        rows.append((x, q, y, r))
        x, y = y, r
    return rows, x

QUOTED = {
    (252, 198): ([(252, 1, 198, 54), (198, 3, 54, 36), (54, 1, 36, 18), (36, 2, 18, 0)], 18, (4, -5)),
    (-35, 15): ([(-35, -3, 15, 10), (15, 1, 10, 5), (10, 2, 5, 0)], 5, (-1, -2)),
    (84, 35): ([(84, 2, 35, 14), (35, 2, 14, 7), (14, 2, 7, 0)], 7, None),
}
for (a, b), (rows, g, coef) in QUOTED.items():
    got_rows, got_g = chain(a, b)
    assert got_rows == rows and got_g == g == math.gcd(a, b)
    if coef:
        assert a * coef[0] + b * coef[1] == g
# the sequence (x_k, y_k) for (252, 198) and K = 4
seq = [(252, 198), (198, 54), (54, 36), (36, 18), (18, 0)]
assert [(r[0], r[2]) for r in chain(252, 198)[0]] + [(18, 0)] == seq
# back-substitution lines
assert 54 - 36 == 18 and 4 * 54 - 198 == 18 and 4 * (252 - 198) - 198 == 18
assert 4 * 252 == 1008 and 5 * 198 == 990 and 1008 - 990 == 18
assert 15 - 10 == 5 and 15 - (-35 + 3 * 15) == 5 and 35 - 30 == 5
# warning
assert 11 * 252 == 2772 == 14 * 198
assert (4 - 11) * 252 + (-5 + 14) * 198 == 18 and -7 * 252 + 9 * 198 == 18
# quick check: gcd(0, -6) = 6
assert max(d for d in range(1, 50) if 0 % d == 0 and -6 % d == 0) == 6 == math.gcd(0, -6)
assert 0 == 0 * 6 + 0
print("ok")
