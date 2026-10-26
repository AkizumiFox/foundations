"""exr-division-with-remainder-r1: f(0) = 0, f(n+1) = f(n) + 2n + 1 gives f(n) = n*n;
the step identity (n+1)(n+1) = (n*n + (n+n)) + 1 = (n*n + 2n) + 1."""
QUOTED = {"f0": 0}
f = QUOTED["f0"]
for n in range(0, 500):
    assert f == n * n
    assert (n + 1) * (n + 1) == (n + 1) * n + (n + 1) == (n * n + n) + (n + 1) == (n * n + (n + n)) + 1
    assert n + n == 2 * n
    f = f + 2 * n + 1
print("ok")
