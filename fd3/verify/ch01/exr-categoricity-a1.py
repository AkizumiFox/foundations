"""exr-categoricity-a1 (c): phi for (N \\ {0}, 1, S) at 0, 1, 2 is 1, 2, 3 (ints, S(n) = n + 1)."""
def S(n): return n + 1
QUOTED = {0: 1, 1: 2, 2: 3}
v = 1
for n in range(3):
    assert v == QUOTED[n]; v = S(v)
print("ok")
