"""exr-finite-sums-b4: sum_{k=1}^{n}(b_{k+1} - b_k) = b_{n+1} - b_1, not b_n - b_1; witness b_k = k, n = 1: left 1, claimed right 0."""
import random
QUOTED = {"left": 1, "claimed_right": 0}
random.seed(10)
for _ in range(300):
    n = random.randint(1, 9)
    b = {k: random.randint(-9, 9) for k in range(1, n + 2)}
    s = sum(b[k + 1] - b[k] for k in range(1, n + 1))
    c = {j: b[j + 1] for j in range(0, n + 1)}
    assert s == sum(c[j + 1] - c[j] for j in range(0, n)) == c[n] - c[0] == b[n + 1] - b[1]
b = lambda k: k
assert b(2) - b(1) == QUOTED["left"] and b(1) - b(1) == QUOTED["claimed_right"]
print("ok")
