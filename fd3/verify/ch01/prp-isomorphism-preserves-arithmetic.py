"""prp-isomorphism-preserves-arithmetic, Quick check: in (N \\ {0}, 1, S) the operation (+)
defined by x (+) 1 = x, x (+) S(y) = S(x (+) y) gives 3 (+) 1 = 3, 3 (+) 2 = 4, 3 (+) 3 = 5,
3 (+) 4 = 6 = phi(5) = phi(2 + 3), while phi(2) + phi(3) = 7 with the + of N."""
def S(n): return n + 1
def oplus(x, y):                     # recursion on y >= 1 with e = 1
    assert y >= 1
    return x if y == 1 else S(oplus(x, y - 1))
def phi(n): return n + 1
QUOTED = {"phi(2+3)": 6, "phi2+phi3": 7, "3(+)k": {1: 3, 2: 4, 3: 5, 4: 6}}
assert phi(2 + 3) == QUOTED["phi(2+3)"]
assert phi(2) + phi(3) == QUOTED["phi2+phi3"]
for k, v in QUOTED["3(+)k"].items(): assert oplus(3, k) == v
assert oplus(phi(2), phi(3)) == phi(5)
for m in range(15):                  # proposition (a) on a sample
    for n in range(15):
        assert phi(m + n) == oplus(phi(m), phi(n))
print("ok")
