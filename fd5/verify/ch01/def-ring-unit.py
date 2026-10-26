"""def-ring-unit: units of Z/6Z are [1], [5] with [5]^{-1} = [5]; [2][x] for x = 0..5 is
[0],[2],[4],[0],[2],[4]; [2][3] = [0]; Z^x = {1, -1} (checked on a window); zero ring."""
QUOTED = {"units6": [1, 5], "inv5": 5, "twice": [0, 2, 4, 0, 2, 4]}
units6 = [a for a in range(6) if any(a * x % 6 == 1 for x in range(6))]
assert units6 == QUOTED["units6"]
assert 5 * QUOTED["inv5"] % 6 == 1
assert [2 * x % 6 for x in range(6)] == QUOTED["twice"] and 2 * 3 % 6 == 0
assert [u for u in range(-50, 51) if any(u * v == 1 for v in range(-50, 51))] == [-1, 1]
print("ok")
