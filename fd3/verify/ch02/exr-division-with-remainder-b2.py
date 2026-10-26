"""exr-division-with-remainder-b2: exactly one of a, a+1, a+2 is divisible by 3; for remainder r = 1
the multiple is a + 2, for r = 2 it is a + 1; 3 does not divide 1 or 2."""
QUOTED = {0: 0, 1: 2, 2: 1}  # remainder r of a -> which of a, a+1, a+2 is the multiple (offset)
for a in range(-200, 201):
    r = a % 3
    hits = [i for i in range(3) if (a + i) % 3 == 0]
    assert hits == [QUOTED[r]]
assert 1 % 3 != 0 and 2 % 3 != 0
print("ok")
