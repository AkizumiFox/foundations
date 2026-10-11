"""def-integer-operations: the warning's values and the Quick check of Section 10.2.
Warning: (1, 0) ~ (2, 1); with (c, d) = (1, 2) the rule [(ac, bd)] gives (1, 0) and
(2, 2), not related; twisted rule [(ad + bc, ac + bd)] at (0, 1), (0, 1) gives (0, 1).
Check: [(2, 5)] * [(4, 1)] = [(13, 22)]; normal forms (0, 3), (3, 0), (0, 9)."""
QUOTED = {
    "bad_outputs": ((1, 0), (2, 2)),
    "twisted": (0, 1),
    "product": (13, 22),
    "normal": {(2, 5): (0, 3), (4, 1): (3, 0), (13, 22): (0, 9)},
}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
mul = lambda p, q: (p[0] * q[0] + p[1] * q[1], p[0] * q[1] + p[1] * q[0])
bad = lambda p, q: (p[0] * q[0], p[1] * q[1])
tw = lambda p, q: (p[0] * q[1] + p[1] * q[0], p[0] * q[0] + p[1] * q[1])


def normal(p):
    a, b = p
    return (a - b, 0) if a >= b else (0, b - a)


assert rel((1, 0), (2, 1))
o1, o2 = bad((1, 0), (1, 2)), bad((2, 1), (1, 2))
assert (o1, o2) == QUOTED["bad_outputs"] and not rel(o1, o2)
assert tw((0, 1), (0, 1)) == QUOTED["twisted"]
# twisted rule is the negative of the product
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                m = mul((a, b), (c, d))
                assert tw((a, b), (c, d)) == (m[1], m[0])
assert mul((2, 5), (4, 1)) == QUOTED["product"]
for p, nf in QUOTED["normal"].items():
    assert normal(p) == nf
assert (-3) * 3 == -9
print("def-integer-operations: OK")
