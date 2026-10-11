"""exr-finite-sets-b1: n -> n+3, n -> n+5, n -> 2n+1 and their inverses."""
QUOTED = {"shifts": [3, 5]}
R = range(0, 5000)
for c in QUOTED["shifts"]:
    assert all((n + c) - c == n and n + c >= c for n in R)
    assert all(m - c >= 0 and (m - c) + c == m for m in range(c, 5000))
assert all((2 * n + 1 - 1) // 2 == n and (2 * n + 1 - 1) % 2 == 0 for n in R)
assert {m for m in range(5000) if m not in (0, 1, 2)} == set(range(3, 5000))
print("ok")
