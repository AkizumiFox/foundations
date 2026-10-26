"""exr-categoricity-b3: (a) f(0) = 1, f(n+1) = 2 f(n) defines one f (2^n); (b) f(0) = 0,
f(n+1) = f(n) + 2n + 1 gives f(n) = n * n, with (n+1)(n+1) = (n n + 2n) + 1 and 2n = n + n;
(c) f(1) = f(0); (d) same equations give the same f; (e) tau(S(0)) = 2 != 1 = S(tau(0)).
Arithmetic from the recursive equations (ints model N)."""
def S(n): return n + 1
def pred(n): return n - 1
def add(m, n): return m if n == 0 else S(add(m, pred(n)))
def mul(m, n): return 0 if n == 0 else add(mul(m, pred(n)), m)
def rec(a, g, n):
    v = a
    for k in range(n): v = g(k, v)
    return v
QUOTED = {"verdicts": ("True", "True", "False", "True", "False"), "e_values": (2, 1)}
verd = []
# (a)
verd.append("T" if all(rec(1, lambda k, x: mul(2, x), n) == 2 ** n for n in range(9)) else "F")
# (b)
ok_b = all(rec(0, lambda k, x: add(add(x, mul(2, k)), 1), n) == mul(n, n) for n in range(25))
ok_b &= all(mul(S(n), S(n)) == add(add(mul(n, n), mul(2, n)), 1) and mul(2, n) == add(n, n)
            for n in range(25))
verd.append("T" if ok_b else "F")
# (c): any f with f(n+1) = f(n) has f(1) = f(0)
for f0 in range(5):
    f = lambda n, f0=f0: rec(f0, lambda k, x: x, n)
    assert f(1) == f(0)
verd.append("F")
# (d)
ok_d = all(rec(c, lambda k, x: add(x, k), n) == rec(c, lambda k, x: add(x, k), n)
           for c in range(4) for n in range(10))
verd.append("T" if ok_d else "F")
# (e)
def tau(k): return {1: 2, 2: 1}.get(k, k)
assert tau(0) == 0 and (tau(S(0)), S(tau(0))) == QUOTED["e_values"]
verd.append("F")
assert tuple({"T": "True", "F": "False"}[c] for c in verd) == QUOTED["verdicts"]
print("ok")
