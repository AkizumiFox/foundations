"""exr-comparing-cardinalities-a1 (b): Schroder-Bernstein run on A = B = N, f = g = 2n."""
QUOTED = {"h": {0: 0, 1: 2, 2: 1, 3: 6, 4: 8}, "C1_start": [4, 12, 20]}

LIMIT = 10_000
f = g = lambda n: 2 * n
gB = {g(b) for b in range(LIMIT)}
C0 = {a for a in range(LIMIT) if a not in gB}
assert all(a % 2 == 1 for a in C0) and C0 == {a for a in range(LIMIT) if a % 2 == 1}
Cs = [C0]
while True:
    nxt = {g(f(a)) for a in Cs[-1] if g(f(a)) < LIMIT}
    if not nxt:
        break
    Cs.append(nxt)
assert sorted(Cs[1])[:3] == QUOTED["C1_start"]
for n, Cn in enumerate(Cs):
    assert Cn == {4**n * q for q in range(1, LIMIT, 2) if 4**n * q < LIMIT}
C = set().union(*Cs)


def h(a):
    if a in C:
        return f(a)
    assert a % 2 == 0
    return a // 2


for a, v in QUOTED["h"].items():
    assert h(a) == v, (a, h(a), v)
# h is injective, and onto an initial segment
vals = [h(a) for a in range(LIMIT // 2)]
assert len(set(vals)) == len(vals)
assert set(range(LIMIT // 8)) <= set(vals)
print("ok")
