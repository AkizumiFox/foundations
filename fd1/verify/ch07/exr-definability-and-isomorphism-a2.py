"""exr-definability-and-isomorphism-a2 (Section 7.5): parts (a), (c), (d), (f), (g), (h), (i),
(k), (l) on windows or by enumeration."""
import itertools, math

Z = range(-30, 31)
# (a) multiples of 3
assert [x for x in Z if any(x == 3 * y for y in range(-30, 31))] == [x for x in Z if x % 3 == 0]
# (c) exists z (x + z = y) in N iff x <= y
assert all(any(x + z == y for z in range(0, 60)) == (x <= y) for x in range(30) for y in range(30))
# (d) forall y not(y < x): {1} in ({1,2,3},<); empty in Z (window: d-1 below d)
assert [x for x in (1, 2, 3) if all(not (y < x) for y in (1, 2, 3))] == [1]
assert all(any(y < x for y in range(-31, 31)) for x in Z)
# (f) exists y (x^2 + y^2 = 1) iff -1 <= x <= 1
for x in [-1.5, -1, -0.3, 0, 0.99, 1, 1.01]:
    assert (1 - x * x >= 0) == (-1 <= x <= 1)
    if -1 <= x <= 1:
        y = math.sqrt(1 - x * x); assert abs(x * x + y * y - 1) < 1e-12
# (g) doubling preserves < both ways
assert all((d < e) == (2 * d < 2 * e) for d in Z for e in Z)
# (h) -d: not order-preserving (0<1, 0>-1); additive
assert 0 < 1 and not (-0 < -1)
assert all(-(d + e) == (-d) + (-e) for d in Z for e in Z)
# (i), (j)
assert -1 != 1 and -0 == 0
# (k) D={a,b,c}, R={(a,c),(b,c)}: automorphisms identity and swap(a,b); {c} defined by exists y R(y,x)
D = "abc"; R = {("a", "c"), ("b", "c")}
A = [dict(zip(D, p)) for p in itertools.permutations(D)
     if all(((x, y) in R) == ((dict(zip(D, p))[x], dict(zip(D, p))[y]) in R) for x in D for y in D)]
assert len(A) == 2 and {"a": "b", "b": "a", "c": "c"} in A
assert [x for x in D if any((y, x) in R for y in D)] == ["c"]
# (l) least element in N, none in Z (window)
assert all(not (y < 0) for y in range(0, 50))
print("exr-definability-and-isomorphism-a2: all quoted values check")
