"""exm-existential-introduction-derivations (Ch 4, Section 4.5): the choices of phi in (a)-(d),
the reading of (b) over Z (R(x, y) as x * y = 1, c = 0), and the arithmetic reading of (d)
(P odd, Q even, f(x) = x + 1, c = 3, witness f(3) = 4)."""
from _s0102_fol import V, C, F, At, And, Ex, sub, free_for

QUOTED = {"(b) witness of exists x R(x, x)": 1, "(d) witness": 4, "(d) c": 3}

x, y, c, x0 = V('x'), V('y'), C('c'), V('x_0')
# (a)
phi = And(At('P', x), At('Q', x))
assert sub(phi, c, 'x') == And(At('P', c), At('Q', c))
# (b) lines 2 and 3 read R(c, c) two ways
assert sub(At('R', x, c), c, 'x') == At('R', c, c) == sub(At('R', x, x), c, 'x')
# (c) phi = R(x_0, y), witness x_0
assert sub(At('R', x0, y), x0, 'y') == At('R', x0, x0) and free_for(x0, 'y', At('R', x0, y))
# (d) phi = Q(y), witness f(c)
assert sub(At('Q', y), F('f', c), 'y') == At('Q', F('f', c))

# (b) over Z: exists x (x * x = 1) true (x = 1); exists x (x * 0 = 1) false
W = range(-100, 101)
assert QUOTED["(b) witness of exists x R(x, x)"] ** 2 == 1
assert not any(d * 0 == 1 for d in W)
# (d) over Z: successor of an odd integer is even; 3 odd; f(3) = 4 even; 3 not even
assert all((d + 1) % 2 == 0 for d in W if d % 2 == 1)
assert QUOTED["(d) c"] % 2 == 1 and QUOTED["(d) c"] + 1 == QUOTED["(d) witness"]
assert QUOTED["(d) witness"] % 2 == 0 and QUOTED["(d) c"] % 2 != 0
# (c) reading over N with <=: every number is at most itself
assert all(d <= d for d in range(0, 100))
print("exm-existential-introduction-derivations: all quoted values check")
