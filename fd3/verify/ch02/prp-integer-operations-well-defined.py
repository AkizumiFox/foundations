"""prp-integer-operations-well-defined: the identities of the proof.

Sum: (a + c) + (b' + d) = (a + b') + (c + d), and (a' + b) + (c + d) = (b + d) + (a' + c).
Product: with H: a + b' = a' + b, the target
  (ac + bd) + (a'd + b'c) - [(ad + bc) + (a'c + b'd)]
equals c*(a + b' - a' - b) - d*(a + b' - a' - b), so it vanishes when H holds;
and the sum of the two multiplied equations rearranges to the target.
Polynomials of degree <= 2 in each variable: checking on {0,1,2}^n proves an identity."""
import itertools

QUOTED = {}

for a, b, a1, b1, c, d in itertools.product(range(3), repeat=6):
    # sum, first argument
    assert (a + c) + (b1 + d) == (a + b1) + (c + d)
    assert (a1 + b) + (c + d) == (b + d) + (a1 + c)
    # product: target difference is (c - d) * (H difference)
    lhs = (a * c + b * d) + (a1 * d + b1 * c)
    rhs = (a * d + b * c) + (a1 * c + b1 * d)
    assert lhs - rhs == (c - d) * ((a + b1) - (a1 + b))
    # the two multiplied equations, added, rearrange to the target
    assert (a * c + b1 * c) + (a1 * d + b * d) == lhs
    assert (a1 * c + b * c) + (a * d + b1 * d) == rhs
    # the multiplied equations themselves
    assert (a + b1) * c == a * c + b1 * c and (a1 + b) * c == a1 * c + b * c
    assert (a1 + b) * d == a1 * d + b * d and (a + b1) * d == a * d + b1 * d
    # symmetry of the formulas in the two pairs
    assert (a * c + b * d, a * d + b * c) == (c * a + d * b, c * b + d * a)

# exhaustive well-definedness on small representatives
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
gp = lambda p, q: (p[0] + q[0], p[1] + q[1])
gm = lambda p, q: (p[0] * q[0] + p[1] * q[1], p[0] * q[1] + p[1] * q[0])
R = range(4)
P = [(x, y) for x in R for y in R]
for p, p1, q, q1 in itertools.product(P, repeat=4):
    if rel(p, p1) and rel(q, q1):
        assert rel(gp(p, q), gp(p1, q1)) and rel(gm(p, q), gm(p1, q1))
        assert rel((p[1], p[0]), (p1[1], p1[0]))
print("prp-integer-operations-well-defined: OK")
