"""lem-power-two-bound: (2*1_F)^k >= (k+1)*1_F; checked in Q for k <= 200, with the step
y + y >= y + 1 for y = k + 1 >= 1."""
QUOTED = {"base": (1, 1)}
p = 1
assert QUOTED["base"] == (p, 0 + 1)
for k in range(200):
    assert p >= k + 1
    y = k + 1
    assert p * 2 >= y * 2 == y + y >= y + 1
    p *= 2
print("ok")
