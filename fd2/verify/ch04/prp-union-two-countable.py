"""prp-union-two-countable claim: each a in N is 2q + r, q in N, r in {0,1}, uniquely;
the interleaving k(2q) = g(q), k(2q+1) = h(q) reaches both lists."""
QUOTED = {}
for a in range(10000):
    reps = [(q, r) for q in range(a + 1) for r in (0, 1) if 2 * q + r == a]
    assert len(reps) == 1
g = lambda q: ("A", q % 7)
h = lambda q: ("B", q % 5)
k = lambda a: g(a // 2) if a % 2 == 0 else h(a // 2)
vals = {k(a) for a in range(100)}
assert {("A", i) for i in range(7)} | {("B", i) for i in range(5)} <= vals
print("ok")
