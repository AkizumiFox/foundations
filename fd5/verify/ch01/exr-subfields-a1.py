"""exr-subfields-a1 and the warning of Section 2.3: in Z/6Z, {[0], [3]} is closed under + and *,
[3] + [3] = [0], [3][3] = [3], it is a field with one [3]; [3][x] lies in {[0], [3]} for every x,
so [3] has no inverse and cannot be canceled in [3][3] = [3][1]."""
QUOTED = {"3+3": 0, "3*3": 3}
n = 6
K = {0, 3}
assert (3 + 3) % n == QUOTED["3+3"]
assert (3 * 3) % n == QUOTED["3*3"]
for a in K:
    for b in K:
        assert (a + b) % n in K and (a * b) % n in K
# [3] acts as the one of K
for a in K:
    assert (a * 3) % n == a
# [3] times anything lies in {0, 3}; never 1
assert {(3 * x) % n for x in range(n)} == {0, 3}
assert (3 * 3) % n == (3 * 1) % n and 3 != 1
print("ok")
