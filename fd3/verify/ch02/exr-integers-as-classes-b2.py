"""exr-integers-as-classes-b2: [(a, b)] = {(y + k, y)} when a = b + k, and
{(x, x + k)} when b = a + k; the examples [(7, 2)], [(2, 7)] with k = 5."""
QUOTED = {"k_72": 5, "k_27": 5}


def rel(p, q):
    return p[0] + q[1] == p[1] + q[0]


M = 30
for a in range(12):
    for b in range(12):
        cls = {(x, y) for x in range(M) for y in range(M) if rel((x, y), (a, b))}
        if b <= a:
            k = a - b
            assert cls == {(y + k, y) for y in range(M) if y + k < M}
        if a <= b:
            k = b - a
            assert cls == {(x, x + k) for x in range(M) if x + k < M}
assert 7 == 2 + QUOTED["k_72"] and 7 == 2 + QUOTED["k_27"]
print("exr-integers-as-classes-b2: OK")
