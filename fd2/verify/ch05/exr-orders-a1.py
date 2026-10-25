"""exr-orders-a1: (c) sup{4,6} = 12 under | (no common multiple among 1..11) and 6 under <=;
(d) lexicographic order on N x N is total (checked on a grid)."""

QUOTED = {"div": 12, "le": 6}

assert [m for m in range(1, 12) if m % 4 == 0 and m % 6 == 0] == []
assert 12 % 4 == 0 and 12 % 6 == 0 and QUOTED["div"] == 12 and max(4, 6) == QUOTED["le"]
lex = lambda p, q: p[0] < q[0] or (p[0] == q[0] and p[1] <= q[1])
G = [(a, b) for a in range(6) for b in range(6)]
assert all(lex(p, q) or lex(q, p) for p in G for q in G)
print("exr-orders-a1: all quoted values check")
