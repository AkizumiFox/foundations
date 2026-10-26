"""exr-quotient-rings-b2: the five subsets, tested on a window of integers."""
QUOTED = {"five": (5, 2, 1, 1, 2), "bez23": (-1, 1)}
W = range(-60, 61)
f, q2, r2, q3, r3 = QUOTED["five"]
assert f == q2 * 2 + r2 == q3 * 3 + r3 and r2 and r3
# (b) 2Z u 3Z not closed under +
assert 5 == 2 * 2 + 1 == 1 * 3 + 2 and 5 % 2 and 5 % 3
# (c) 4Z + 6Z = 2Z
S = {4 * x + 6 * y for x in range(-30, 31) for y in range(-30, 31)}
assert all((n in S) == (n % 2 == 0) for n in W)
for k in W:
    assert 2 * k == 4 * (-k) + 6 * k
# (e) {n : 6 | n^2} = 6Z
assert all(((n * n) % 6 == 0) == (n % 6 == 0) for n in range(-500, 501))
x, y = QUOTED["bez23"]
assert 1 == x * 2 + y * 3
print("exr-quotient-rings-b2: ok")
