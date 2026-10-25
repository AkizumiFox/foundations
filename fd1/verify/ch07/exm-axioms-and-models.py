"""exm-axioms-and-models (Section 7.4): every model and non-model of the gallery, on its
stated domain or a window of Z, N, Q; the two-element field against (F1)-(F9) and (1 != 0)."""
import itertools
import sys
from fractions import Fraction as F
sys.path.insert(0, "verify/ch07")
from _rel_props import refl, sym, trans, antisym, conn, irrefl

QUOTED = {"abs_trans_fail": (0, 1, 2), "Z_F8_fail": 2, "N_inv_fail": 1, "dense_fail": (0, 1)}

# equivalence relation on {a,b,c}
D = "abc"
R = {("a", "a"), ("b", "b"), ("c", "c"), ("a", "b"), ("b", "a")}
assert refl(D, R) and sym(D, R) and trans(D, R)
W = range(-6, 7)
par = {(x, y) for x in W for y in W if (x - y) % 2 == 0}
assert refl(W, par) and sym(W, par) and trans(W, par)
near = {(x, y) for x in W for y in W if abs(x - y) <= 1}
assert refl(W, near) and sym(W, near) and not trans(W, near)
x, y, z = QUOTED["abs_trans_fail"]
assert (x, y) in near and (y, z) in near and (x, z) not in near

# partial and linear orders
Dv = [1, 2, 3, 6]
div = {(p, q) for p in Dv for q in Dv if q % p == 0}
assert refl(Dv, div) and antisym(Dv, div) and trans(Dv, div) and not conn(Dv, div)
assert (2, 3) not in div and (3, 2) not in div
N = range(0, 15)
le = {(p, q) for p in N for q in N if p <= q}
assert refl(N, le) and antisym(N, le) and trans(N, le) and conn(N, le)
A = "ab"
anti = {("a", "a"), ("b", "b")}
assert refl(A, anti) and antisym(A, anti) and trans(A, anti) and not conn(A, anti)

# strict, dense orders
Q = sorted({F(p, q) for p in range(-8, 9) for q in range(1, 5)})
lt = {(p, q) for p in Q for q in Q if p < q}
assert irrefl(Q, lt) and trans(Q, lt)
assert all(p < (p + q) / 2 < q for p, q in lt)
a, b = QUOTED["dense_fail"]
assert not any(a < k < b for k in range(-10, 11))

# groups: (Z,+,0) inverses in a window, (N,+,0) fails (Inv) at 1
assert all(d + (-d) == 0 for d in range(-20, 21))
assert not any(QUOTED["N_inv_fail"] + n == 0 for n in range(0, 100))

# two-element field
E = [0, 1]
add = lambda u, v: (u + v) % 2
mul = lambda u, v: u * v
assert [add(0, 0), add(0, 1), add(1, 0), add(1, 1)] == [0, 1, 1, 0]
assert [mul(0, 0), mul(0, 1), mul(1, 0), mul(1, 1)] == [0, 0, 0, 1]
for u, v, w in itertools.product(E, repeat=3):
    assert add(add(u, v), w) == add(u, add(v, w))          # F2
    assert mul(mul(u, v), w) == mul(u, mul(v, w))          # F5
    assert mul(u, add(v, w)) == add(mul(u, v), mul(u, w))  # F9
for u, v in itertools.product(E, repeat=2):
    assert add(u, v) == add(v, u) and mul(u, v) == mul(v, u)  # F1, F6
for u in E:
    assert add(u, 0) == u and mul(u, 1) == u                   # F3, F7
    assert any(add(u, v) == 0 for v in E)                      # F4
    assert u == 0 or any(mul(u, v) == 1 for v in E)            # F8
assert 0 != 1                                                  # (1 != 0)
# Z fails F8 at 2
assert not any(QUOTED["Z_F8_fail"] * k == 1 for k in range(-100, 101))
print("exm-axioms-and-models: all quoted values check")
