"""prp-naturals-in-ordered-field (a)-(c) in F = Q, from the recursion n.1 (0.1 = 0, (n+1).1 = n.1 + 1); def examples."""
from fractions import Fraction as Fr

QUOTED = {"one_times_one": 1, "two_times_one": 2}

def mult(n, a=Fr(1)):
    y = Fr(0)
    for _ in range(n):
        y = y + a
    return y

def power(x, k):
    y = Fr(1)
    for _ in range(k):
        y = y * x
    return y

assert mult(1) == QUOTED["one_times_one"] and mult(2) == QUOTED["two_times_one"] == 1 + 1
for m in range(12):
    for n in range(12):
        assert mult(m + n) == mult(m) + mult(n)
        assert mult(m * n) == mult(m) * mult(n)
        if m < n:
            assert mult(m) < mult(n)
    if m >= 1:
        assert mult(m) >= 1
for n in range(6):
    for k in range(6):
        assert mult(n ** k) == power(mult(n), k)
assert power(Fr(0), 0) == 1
print("ok")
