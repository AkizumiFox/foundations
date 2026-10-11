"""exr-infinite-sets-b3: X = N, Y = 2N; X \\ Y is the odd numbers, listed by n -> 2n + 1."""
QUOTED = {"missing_from_Y": 1}

N = 10_000
Y = {2 * n for n in range(N)}
assert QUOTED["missing_from_Y"] not in Y
odds = [2 * n + 1 for n in range(N)]
assert set(odds) == {m for m in range(2 * N) if m not in Y}
assert len(set(odds)) == N
print("ok")
