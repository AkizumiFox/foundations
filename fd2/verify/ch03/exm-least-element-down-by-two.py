"""exm-least-element-down-by-two (Ch 2, 01): S closed under s -> s-2 (s >= 2) contains 0 or 1;
Quick check: {17 - 5k : 5k <= 17} = {17, 12, 7, 2}, least element 2 = 17 mod 5."""
import random
random.seed(1)
for _ in range(20000):
    S = set(random.sample(range(41), random.randint(1, 8)))
    # close downward under s -> s - 2
    stack = list(S)
    while stack:
        s = stack.pop()
        if s >= 2 and s - 2 not in S:
            S.add(s - 2); stack.append(s - 2)
    assert all(s - 2 in S for s in S if s >= 2)
    assert min(S) in (0, 1) and (0 in S or 1 in S)
QUOTED = {"S": [17, 12, 7, 2], "ks": [0, 1, 2, 3], "least": 2}
ks = [k for k in range(100) if 5 * k <= 17]
assert ks == QUOTED["ks"]
S = [17 - 5 * k for k in ks]
assert S == QUOTED["S"] and min(S) == QUOTED["least"] == 17 % 5 and 17 == 5 * 3 + 2
assert 5 * 3 == 15 <= 17 < 20 == 5 * 4
print("exm-least-element-down-by-two: all quoted values check")
