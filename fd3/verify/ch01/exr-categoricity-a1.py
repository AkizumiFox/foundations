"""exr-categoricity-a1 (c): phi for (omega \\ {0}, 1, S) at 0, 1, 2 is 1, 2, 3."""
E = frozenset()
def S(x): return x | frozenset([x])
def num(k):
    x = E
    for _ in range(k): x = S(x)
    return x
QUOTED = {0: 1, 1: 2, 2: 3}
v = num(1)
for n in range(3):
    assert v == num(QUOTED[n]); v = S(v)
print("ok")
