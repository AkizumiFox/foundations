"""exr-universal-introduction-a1 (Section 5.4): readings over Z for D1 and D3."""
QUOTED = {"x_0 names": 2, "odd witness": 1}
even = lambda n: n % 2 == 0
# D1: forall x (P(x) -> Q(x)) with P = Q = even is true; P(x_0) true; forall x Q(x) false.
Z = range(-100, 100)
assert all((not even(n)) or even(n) for n in Z)
assert even(QUOTED["x_0 names"]) and not even(QUOTED["odd witness"])
# D3: R(x_0, c) -> forall x R(x, c) with R as <, c = 5, x_0 = 1: hypothesis 1 < 5 true,
# conclusion "every integer is below 5" false (6).
c, x0 = 5, 1
assert x0 < c and not all(n < c for n in Z) and not (6 < c)
print("exr-universal-introduction-a1: all quoted values check")
