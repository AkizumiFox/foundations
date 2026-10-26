"""prp-naturals-in-ordered-field (a)-(c) in F = Q, from the recursion n.1 (0.1 = 0, (n+1).1 = n.1 + 1); def examples;
the Quick check after the proposition: (3.1)(4.1) - 5.1 = 7.1, via 12 = 7 + 5, and 7.1 >= 1 > 0."""
from fractions import Fraction as Fr

QUOTED = {"one_times_one": 1, "two_times_one": 2,
          "qc_product": 12, "qc_result": 7}

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
# Quick check: product law gives 12.1, sum law splits 12 = 7 + 5, result 7.1, positive
assert 3 * 4 == QUOTED["qc_product"] and mult(3) * mult(4) == mult(QUOTED["qc_product"])
assert QUOTED["qc_product"] == QUOTED["qc_result"] + 5
assert mult(QUOTED["qc_product"]) == mult(QUOTED["qc_result"]) + mult(5)
assert mult(3) * mult(4) - mult(5) == mult(QUOTED["qc_result"])
assert mult(QUOTED["qc_result"]) >= 1 > 0
# the same in a field of characteristic 0 other than Q: Q(sqrt2) represented as pairs (a, b) = a + b sqrt2
def mult2(n):
    y = (Fr(0), Fr(0))
    for _ in range(n):
        y = (y[0] + 1, y[1])
    return y
def mul2(u, v):
    return (u[0]*v[0] + 2*u[1]*v[1], u[0]*v[1] + u[1]*v[0])
p34 = mul2(mult2(3), mult2(4))
assert (p34[0] - mult2(5)[0], p34[1] - mult2(5)[1]) == mult2(7)
print("ok")
