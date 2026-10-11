"""prp-binomial-absorption: (k + 1) C(n + 1, k + 1) = (n + 1) C(n, k) for n, k < 30 (Pascal
table); idea instances 1*3 = 3*1 (n = 2, k = 0) and 2*6 = 4*3 (n = 3, k = 1)."""
QUOTED = {"inst1": (1, 3, 3, 1), "inst2": (2, 6, 4, 3)}
N = 32
C = [[1 if k == 0 else 0 for k in range(N + 2)]]
for n in range(N):
    prev = C[-1]
    C.append([1] + [prev[k] + prev[k + 1] for k in range(N + 1)])
for n in range(30):
    for k in range(30):
        assert (k + 1) * C[n + 1][k + 1] == (n + 1) * C[n][k]
a, b, c, d = QUOTED["inst1"]
assert (a, b) == (1, C[3][1]) and (c, d) == (3, C[2][0]) and a * b == c * d
a, b, c, d = QUOTED["inst2"]
assert (a, b) == (2, C[4][2]) and (c, d) == (4, C[3][1]) and a * b == c * d
print("ok")
