"""exr-ordered-rings-b2 (Section 10.3): [(0, 1)] . [(0, 1)] = [(1, 0)], not in P'."""
def mul(x, y):
    return (x[0] * y[0] + x[1] * y[1], x[0] * y[1] + x[1] * y[0])


QUOTED = {"square": (1, 0)}
sq = mul((0, 1), (0, 1))
assert sq == QUOTED["square"]
assert 0 < 1 and not (sq[0] < sq[1])
# sums of elements of P' stay in P' (a < b, c < d => a + c < b + d), on a grid
G = range(0, 7)
assert all(a + c < b + d for a in G for b in G for c in G for d in G if a < b and c < d)
print("exr-ordered-rings-b2: all quoted values check")
