"""exr-integers-as-classes-a1: (b) the only pair with a coordinate 0 in [(6, 9)]
is (0, 3); (d) (1, 1) ~ (5, 5)."""
QUOTED = {"b": [(0, 3)], "d": True}


def rel(p, q):
    return p[0] + q[1] == p[1] + q[0]


found = [p for n in range(100) for p in {(n, 0), (0, n)} if rel(p, (6, 9))]
assert sorted(set(found)) == QUOTED["b"], found
assert 9 == 3 + 6 and 6 < 9
assert rel((1, 1), (5, 5)) == QUOTED["d"]
print("exr-integers-as-classes-a1: OK")
