"""exm-integer-pair-classes: the elements with first coordinate <= 4 of
[(3, 5)], [(0, 0)], [(4, 1)], and the descriptions y = x + 2, x = y, x = y + 3."""

QUOTED = {
    (3, 5): [(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)],
    (0, 0): [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
    (4, 1): [(3, 0), (4, 1)],
}


def rel(p, q):
    return p[0] + q[1] == p[1] + q[0]


N = 60  # second coordinates never exceed x + 2 <= 6 for x <= 4
for rep, listed in QUOTED.items():
    found = [(x, y) for x in range(5) for y in range(N) if rel((x, y), rep)]
    assert found == listed, (rep, found)

for x in range(50):
    for y in range(50):
        assert rel((x, y), (3, 5)) == (y == x + 2)
        assert rel((x, y), (0, 0)) == (x == y)
        assert rel((x, y), (4, 1)) == (x == y + 3)
print("exm-integer-pair-classes: OK")
