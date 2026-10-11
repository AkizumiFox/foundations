"""Gate 0, P3: the identity in (a), the truth of the claim, and the counterexamples to the steps."""
QUOTED = {"points_a": [1, 2, 1, 1], "points_b": [1, 2, 1, 1]}
assert sum(QUOTED["points_a"]) == 5 and sum(QUOTED["points_b"]) == 5

for n in range(0, 2000):
    assert (n + 1) ** 2 + (n + 1) == (n * n + n) + 2 * (n + 1) == n * n + 3 * n + 2
    assert (n * n + n) % 2 == 0
    q, r = divmod(n, 2)
    if r == 0:
        assert n * n + n == 2 * (q * (n + 1))
    else:
        assert n + 1 == 2 * (q + 1) and n * n + n == 2 * (n * (q + 1))

# (a) counterexample to the inference: P(n) := (n == 0)
P = lambda n: n == 0
N = range(0, 50)
forall_P = all(P(n) for n in N)
assert P(0) and not forall_P
premise2 = (not forall_P) or all(P(n + 1) for n in N)   # vacuously true
assert premise2

# (b) M_n = n: each has a larger number (n + 1), none bounds all of 0..K for M <= K - 1
for K in range(1, 200):
    M = K - 1
    assert any(n >= M + 1 for n in range(K + 1))
print("ok")
