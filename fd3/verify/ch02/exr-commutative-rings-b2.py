"""exr-commutative-rings-b2 (prove or disprove).
(a) -(x+y) and (-x)+(-y) are both the class of (b+d, a+c).
(b) in Z x Z (componentwise), (1,0)(1,0) = (1,0), neither (0,0) nor (1,1): idempotent counterexample;
    second illustration in Z/6, [3][3] = [9] = [3] (9 - 3 = 6), [3] not [0], [1].
(c) N x N with coordinatewise + and the cross product: the only additive zero is (0,0),
    and (1,0) + (x,y) = (1+x, y) is never (0,0): (F4) fails.
(d) a + b = a forces b = 0 (checked in Z/n for small n as an illustration)."""
import itertools
add = lambda p, q: (p[0] + q[0], p[1] + q[1])
neg = lambda p: (p[1], p[0])
R = range(8)
for a, b, c, d in itertools.product(R, repeat=4):
    assert neg(add((a, b), (c, d))) == (b + d, a + c) == add(neg((a, b)), neg((c, d)))
QUOTED = {"b_square": 9, "b_diff": 6}
assert 3 * 3 == QUOTED["b_square"] and QUOTED["b_square"] - 3 == QUOTED["b_diff"]
assert (3 * 3) % 6 == 3 and 3 % 6 not in (0, 1)
mul2 = lambda p, q: (p[0] * q[0], p[1] * q[1])
assert mul2((1, 0), (1, 0)) == (1, 0) and (1, 0) not in ((0, 0), (1, 1))
# exr-commutative-rings-a1 (c): (1,0)(0,1) = (0,0) in Z x Z
assert mul2((1, 0), (0, 1)) == (0, 0)
# (c) zeros: z with p + z = p for all p in a box; only (0,0)
zeros = [z for z in itertools.product(range(10), repeat=2)
         if all(add(p, z) == p for p in itertools.product(range(5), repeat=2))]
assert zeros == [(0, 0)]
assert add((0, 0), (3, 4)) == (3, 4)
assert all(add((1, 0), (x, y)) != (0, 0) for x, y in itertools.product(range(50), repeat=2))
for n in range(1, 13):
    for a, b in itertools.product(range(n), repeat=2):
        if (a + b) % n == a:
            assert b == 0
print("exr-commutative-rings-b2: OK")
