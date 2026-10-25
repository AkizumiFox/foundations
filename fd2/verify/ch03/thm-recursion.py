"""thm-recursion: quick check, a = 1, g(n, x) = 2x + 1 gives 1, 3, 7, 15 and stays in N."""
QUOTED = [1, 3, 7, 15]
f = [1]
for n in range(30):
    x = f[-1]
    assert isinstance(x, int) and x >= 0
    f.append(2 * x + 1)
assert f[:4] == QUOTED
print("ok")
