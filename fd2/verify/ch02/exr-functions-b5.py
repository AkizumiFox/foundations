"""exr-functions-b5 (a)-(e) (F2.6 §02)."""
import math
QUOTED = {"g(0)": 0, "g(1)": 0}

# (a) counterexample
f = {1: 1}; g = {1: 1, 2: 1}
gf = {x: g[f[x]] for x in f}
assert len(set(gf.values())) == len(gf) and set(g.values()) == {1} and 2 not in f.values()
# (b) f(n) = 2n, g halving by parity, on N
fb = lambda n: 2 * n
gb = lambda m: m // 2 if m % 2 == 0 else (m - 1) // 2
assert all(gb(m) >= 0 and (2 * gb(m) == m or 2 * gb(m) + 1 == m) for m in range(500))
assert all(gb(fb(n)) == n for n in range(500))
assert gb(0) == QUOTED["g(0)"] and gb(1) == QUOTED["g(1)"]
# (d) id vs abs agree on squares, differ at -1, differ exactly on negatives
xs = [k / 3 for k in range(-60, 61)]
assert all(x * x == abs(x * x) for x in xs)
assert -1 != abs(-1)
assert all((t != abs(t)) == (t < 0) for t in xs)
# (c), (e): t -> t^3 injective (strictly increasing) and onto (numeric cube roots)
assert all(a ** 3 < b ** 3 for a in xs for b in xs if a < b)
for y in xs:
    r = math.copysign(abs(y) ** (1 / 3), y)
    assert abs(r ** 3 - y) < 1e-9
print("exr-functions-b5: all statements check")
