"""def-integers-as-classes: the Quick check of Section 10.1, the non-example
(a, b) ~ (c, d) iff ad = bc on N x N, and the normal forms quoted in the check."""
import sys

QUOTED = {
    "check_1": ((2, 7), (10, 15), True, 17, 17),
    "check_2": ((2, 7), (15, 10), False, 12, 22),
    "nonexample": [((1, 1), (0, 0), True), ((0, 0), (2, 1), True), ((1, 1), (2, 1), False)],
    "normal_forms": {(2, 7): (0, 5), (10, 15): (0, 5), (15, 10): (5, 0)},
}


def rel(p, q):
    (a, b), (c, d) = p, q
    return a + d == b + c


def prod_rel(p, q):
    (a, b), (c, d) = p, q
    return a * d == b * c


def normal(p):
    a, b = p
    return (a - b, 0) if a >= b else (0, b - a)


for key in ("check_1", "check_2"):
    p, q, related, s1, s2 = QUOTED[key]
    assert rel(p, q) == related, key
    assert p[0] + q[1] == s1 and p[1] + q[0] == s2, key

for p, q, related in QUOTED["nonexample"]:
    assert prod_rel(p, q) == related, (p, q)
# reflexive and symmetric on a grid, not transitive (witnessed above)
R = range(6)
pairs = [(a, b) for a in R for b in R]
assert all(prod_rel(p, p) for p in pairs)
assert all(prod_rel(q, p) for p in pairs for q in pairs if prod_rel(p, q))

for p, nf in QUOTED["normal_forms"].items():
    assert normal(p) == nf and rel(p, nf), p
print("def-integers-as-classes: OK")
sys.exit(0)
