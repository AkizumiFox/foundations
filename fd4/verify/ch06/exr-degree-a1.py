"""exr-degree-a1: (b) m = 1, n = 2, m + n = 3, (pq)_3 = 2 * 3 = 6 over Z and [0] over Z/6Z; (c) x + (-x) = 0."""
QUOTED = {"m, n, m+n": (1, 2, 3), "(pq)_3": 6}

p, q = [1, 2], [0, 1, 3]
m, n = len(p) - 1, len(q) - 1
assert (m, n, m + n) == QUOTED["m, n, m+n"]
pq = [sum(p[i] * q[k - i] for i in range(k + 1) if i < len(p) and 0 <= k - i < len(q)) for k in range(4)]
assert pq[3] == p[1] * q[2] == QUOTED["(pq)_3"] and pq[3] % 6 == 0
assert [a + b for a, b in zip([0, 1], [0, -1])] == [0, 0]
print("exr-degree-a1: ok")
