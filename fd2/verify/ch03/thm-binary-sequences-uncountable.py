"""thm-binary-sequences-uncountable: the table before it (rows f(0)..f(3), places 0..4) and
the flipped diagonal g = 1, 0, 1, 0; also the Quick check: for f(n) = ind_{n}, g is zero."""

QUOTED = {
    "rows": [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 1, 1]],
    "g": [1, 0, 1, 0],
}

rows = QUOTED["rows"]
g = [1 - rows[n][n] for n in range(4)]
assert g == QUOTED["g"]
for n in range(4):
    assert g[n] != rows[n][n] and g != rows[n][:4]
# Quick check: f(n) = indicator of {n}
N = 30
f = [[1 if k == n else 0 for k in range(N)] for n in range(N)]
gq = [1 - f[n][n] for n in range(N)]
assert gq == [0] * N and all(f[n] != gq for n in range(N))
print("thm-binary-sequences-uncountable: all quoted values check")
