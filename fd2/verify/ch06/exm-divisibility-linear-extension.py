"""exm-divisibility-linear-extension: x [= y iff y = 0 or (x != 0 and x <= y), on
{0..30}: partial order, total, contains divisibility; 2 | 0 but not 2 <= 0. Quick
check: the order of 0, 1, 4, 6, 12, and the only pair comparable under [= but not |."""
N = range(31)


def le(x, y):
    return y == 0 or (x != 0 and x <= y)


def div(a, b):
    return b == 0 if a == 0 else b % a == 0


assert all(le(x, x) for x in N)
assert all(x == y for x in N for y in N if le(x, y) and le(y, x))
assert all(le(x, z) for x in N for y in N for z in N if le(x, y) and le(y, z))
assert all(le(x, y) or le(y, x) for x in N for y in N)
assert all(le(a, b) for a in N for b in N if div(a, b))
assert div(2, 0) and not 2 <= 0
S = [0, 1, 4, 6, 12]
from functools import cmp_to_key
order = sorted(S, key=cmp_to_key(lambda x, y: 0 if x == y else (-1 if le(x, y) else 1)))
assert order == [1, 4, 6, 12, 0]
bad = {(x, y) for x in S for y in S if x < y and not (div(x, y) or div(y, x))}
assert bad == {(4, 6)}
print("exm-divisibility-linear-extension: ok")
