"""exr-infinite-sets-c1: the plain diagonal can fail to be increasing; the given g works."""
import random

QUOTED = {"plain_g0": 6, "plain_g1": 2}

f0 = lambda n: 5 + n
f1 = lambda n: n
plain = [f0(0) + 1, f1(1) + 1]
assert plain == [QUOTED["plain_g0"], QUOTED["plain_g1"]] and plain[0] > plain[1]

random.seed(1)
for trial in range(200):
    # random strictly increasing functions, as lists of values on 0..L-1
    L = 30
    fs = []
    for _ in range(L):
        v, vals = random.randint(0, 5), []
        for _ in range(L):
            vals.append(v)
            v += random.randint(1, 4)
        fs.append(vals)
    g = [fs[0][0] + 1]
    for n in range(L - 1):
        g.append(max(g[n], fs[n + 1][n + 1]) + 1)
    assert all(g[n] < g[n + 1] for n in range(L - 1))
    assert all(g[n] > fs[n][n] for n in range(L))
print("ok")
