"""def-power: the sqrt 2 recursion values, and the 1/(a_n - 1) breakdown in the warning."""
from fractions import Fraction as Fr

QUOTED = {"a": [Fr(2), Fr(3, 2), Fr(17, 12)], "a2_sq": Fr(289, 144), "excess": Fr(1, 144),
          "bad_a1": 1, "fib_like_1": [0, 1, 1, 2], "fib_like_2": [2, 1, 3, 4]}

a = [Fr(2)]
for _ in range(5):
    x = a[-1]
    assert x > 0
    a.append((x + 2 / x) / 2)
assert a[:3] == QUOTED["a"]
assert a[2] ** 2 == QUOTED["a2_sq"] and a[2] ** 2 - 2 == QUOTED["excess"]
# g maps (0, inf) to (0, inf) on a sample
for x in [Fr(1, 1000), Fr(1, 3), Fr(1), Fr(5), Fr(10**6)]:
    assert (x + 2 / x) / 2 > 0
# the broken recursion a0 = 2, a_{n+1} = 1/(a_n - 1)
a1 = 1 / (Fr(2) - 1)
assert a1 == QUOTED["bad_a1"] and a1 - 1 == 0
# two sequences obeying a_{n+2} = a_{n+1} + a_n
for s in (QUOTED["fib_like_1"], QUOTED["fib_like_2"]):
    assert all(s[i + 2] == s[i + 1] + s[i] for i in range(len(s) - 2))
print("ok")
