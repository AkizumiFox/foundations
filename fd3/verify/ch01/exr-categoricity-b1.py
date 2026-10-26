"""exr-categoricity-b1: (E, 0, x -> x + 2) with E the even numbers; phi(n) = 2n, and
2 * S(n) = 2n + 2, 2n + 2 = S(2n + 1) != 0, x + 2 injective. Arithmetic from the recursive
equations (ints model N, S(n) = n + 1)."""
def S(n): return n + 1
def pred(n): return n - 1
def add(m, n): return m if n == 0 else S(add(m, pred(n)))
def mul(m, n): return 0 if n == 0 else add(mul(m, pred(n)), m)
QUOTED = {"phi(n)": "2n"}
RANGE = 12
v = 0                          # phi(0) = e = 0
evens = set()
for n in range(RANGE):
    assert v == mul(2, n) == 2 * n
    assert mul(2, S(n)) == add(mul(2, n), 2)                 # 2 S(n) = 2n + 2
    assert add(v, 2) == S(add(v, 1)) != 0                    # (P3)
    evens.add(v); v = add(v, 2)                              # s(x) = x + 2
assert len({add(x, 2) for x in evens}) == len(evens)         # (P4) on the sample
print("ok")
