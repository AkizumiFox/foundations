"""exr-categoricity-b1: (E, 0, x -> x + 2) with E the even numbers; phi(n) = 2n, and
2 * S(n) = 2n + 2, 2n + 2 = S(2n + 1) != 0, x + 2 injective. Arithmetic from the recursive
equations on von Neumann numerals."""
E0 = frozenset()
def S(x): return x | frozenset([x])
def pred(x): return frozenset().union(*x) if x else E0   # union of S(k) is k
def num(k):
    x = E0
    for _ in range(k): x = S(x)
    return x
def add(m, n): return m if n == E0 else S(add(m, pred(n)))
def mul(m, n): return E0 if n == E0 else add(mul(m, pred(n)), m)
QUOTED = {"phi(n)": "2n"}
RANGE = 9
two = num(2)
v = E0                         # phi(0) = e = 0
evens = set()
for n in range(RANGE):
    assert v == mul(two, num(n)) == num(2 * n)
    assert mul(two, S(num(n))) == add(mul(two, num(n)), two)        # 2 S(n) = 2n + 2
    assert add(v, two) == S(add(v, num(1))) != E0                   # (P3)
    evens.add(v); v = add(v, two)                                   # s(x) = x + 2
assert len({add(x, two) for x in evens}) == len(evens)              # (P4) on the sample
print("ok")
