"""exr-categoricity-b2: phi(3) = 3 in Chapter 7's N; 2 * 3 = 6 in omega from the recursive
equations, with the intermediate sums 0 + 2 = 2, 2 + 2 = 4, 4 + 2 = 6; phi(6) = 6."""
E0 = frozenset()
def S(x): return x | frozenset([x])
def pred(x): return frozenset().union(*x) if x else E0
def num(k):
    x = E0
    for _ in range(k): x = S(x)
    return x
def add(m, n): return m if n == E0 else S(add(m, pred(n)))
def mul(m, n): return E0 if n == E0 else add(mul(m, pred(n)), m)
QUOTED = {"phi3": 3, "prod": 6, "steps": [(0, 2, 2), (2, 2, 4), (4, 2, 6)], "phi6": 6}
def phi(n):      # phi(0) = 0, phi(S(n)) = phi(n) + 1 in N (integers)
    return 0 if n == E0 else phi(pred(n)) + 1
assert phi(num(3)) == QUOTED["phi3"] == ((0 + 1) + 1) + 1
assert mul(num(2), num(3)) == num(QUOTED["prod"])
assert mul(num(2), num(0)) == E0
for a, b, c in QUOTED["steps"]:
    assert add(num(a), num(b)) == num(c)
assert phi(mul(num(2), num(3))) == QUOTED["phi6"] == phi(num(2)) * phi(num(3))
print("ok")
