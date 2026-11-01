"""prp-binomial-factorial: (a) C(n,k) k! (n-k)! = n!, (b) symmetry, (c) C(n,k) k! = prod_{j<k}(n-j)
for n < 40 (Pascal table); the Quick check: row 7 and 7!/(3! 4!) = 5040/144 = 35."""
from math import factorial, prod
QUOTED = {"row7": [1, 7, 21, 35, 35, 21, 7, 1], "fact7": 5040, "denom": (6, 24, 144), "c73": 35}
N = 40
C = [[1 if k == 0 else 0 for k in range(N + 2)]]
for n in range(N):
    prev = C[-1]
    C.append([1] + [prev[k] + prev[k + 1] for k in range(N + 1)])
for n in range(N):
    for k in range(n + 1):
        assert C[n][k] * factorial(k) * factorial(n - k) == factorial(n)
        assert C[n][k] == C[n][n - k]
        assert C[n][k] * factorial(k) == prod(n - j for j in range(k))
        assert factorial(n) == factorial(n - k) * prod(n - j for j in range(k))
assert C[7][:8] == QUOTED["row7"]
assert C[7][3] == C[6][2] + C[6][3] == 15 + 20
assert factorial(7) == QUOTED["fact7"]
a, b, c = QUOTED["denom"]
assert (a, b, c) == (factorial(3), factorial(4), factorial(3) * factorial(4))
assert QUOTED["fact7"] // c == QUOTED["c73"] and QUOTED["fact7"] % c == 0 and C[7][3] == 35
print("ok")
