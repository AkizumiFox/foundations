"""exm-integer-laws-two-routes: with x = [(a,b)], y = [(c,d)],
-x = [(b,a)], (-x)y = [(bc+ad, bd+ac)], xy = [(ac+bd, ad+bc)], -(xy) = [(ad+bc, ac+bd)],
and the two pairs are equal after reordering sums (commutativity of + in N).
Also the quick check after the remark: -[(2,7)] = [(7,2)], and every (c,d) with
(2+c, 7+d) ~ (0,0) has c = 5 + d and (c,d) ~ (7,2)."""
import itertools
mul = lambda p, q: (p[0] * q[0] + p[1] * q[1], p[0] * q[1] + p[1] * q[0])
neg = lambda p: (p[1], p[0])
add = lambda p, q: (p[0] + q[0], p[1] + q[1])
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
R = range(7)
for a, b, c, d in itertools.product(R, repeat=4):
    x, y = (a, b), (c, d)
    assert mul(neg(x), y) == (b * c + a * d, b * d + a * c)
    assert mul(x, y) == (a * c + b * d, a * d + b * c)
    assert neg(mul(x, y)) == (a * d + b * c, a * c + b * d)
    assert mul(neg(x), y) == neg(mul(x, y))          # equal pairs, not merely related
QUOTED = {"negative": (7, 2)}
assert neg((2, 7)) == QUOTED["negative"]
for c, d in itertools.product(range(40), repeat=2):
    if rel(add((2, 7), (c, d)), (0, 0)):
        assert c == 5 + d and rel((c, d), (7, 2))
assert rel(add((2, 7), (7, 2)), (0, 0))
print("exm-integer-laws-two-routes: OK")
