"""exr-orders-c1: the lexicographic order on N x N is a partial order and every non-empty subset of a
grid has a least element given by (least first coordinate, then least second); (1, n) < (2, 1)."""
import random

QUOTED = {"top": (2, 1)}

lex = lambda p, q: p[0] < q[0] or (p[0] == q[0] and p[1] <= q[1])
G = [(a, b) for a in range(5) for b in range(5)]
assert all(lex(p, p) for p in G)
assert all(p == q for p in G for q in G if lex(p, q) and lex(q, p))
assert all(lex(p, r) for p in G for q in G for r in G if lex(p, q) and lex(q, r))
random.seed(7)
for _ in range(2000):
    S = random.sample(G, random.randint(1, len(G)))
    a0 = min(a for a, _ in S)
    b0 = min(b for a, b in S if a == a0)
    assert (a0, b0) in S and all(lex((a0, b0), s) for s in S)
assert all(lex((1, n), QUOTED["top"]) and (1, n) != QUOTED["top"] for n in range(1000))
print("exr-orders-c1: all quoted values check")
