"""exr-universal-introduction-a1 (Ch 4, Section 4.4): readings over Z for D1 and D3."""
QUOTED = {"x_0 names": 2, "odd witness": 1}
even = lambda n: n % 2 == 0
# D1: forall x (P(x) -> Q(x)) with P = Q = even is true; P(x_0) true; forall x Q(x) false.
Z = range(-100, 100)
assert all((not even(n)) or even(n) for n in Z)
assert even(QUOTED["x_0 names"]) and not even(QUOTED["odd witness"])
# D3: P(x_0) -> forall x P(x): hypothesis true at 2, conclusion false at 1.
assert even(2) and not all(even(n) for n in Z)
print("exr-universal-introduction-a1: all quoted values check")
