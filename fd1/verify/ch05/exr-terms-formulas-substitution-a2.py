"""exr-terms-formulas-substitution-a2 (Section 5.2), with the paragraph "One substitution at a
time" and its Quick check, and the Quick check after "Before you substitute"."""
from _s0102_fol import *

QUOTED = {"(a) FV": {"x", "y"}, "(b) sentence": True, "(c) FV of the slip": {"x"},
          "(d) FV after repair": {"a"}, "(h) swap?": False, "QC1 swap": "P(y) \\wedge Q(x)",
          "QC2 y free for x": False, "QC2 x + 1 free for x": True}

x, y, z, u, a, c = V('x'), V('y'), V('z'), V('u'), V('a'), C('c')
def plus(s, t): return F('+', s, t)
def sub2(p, t1, x1, t2, x2): return sub(sub(p, t1, x1), t2, x2)

# paragraph: R(x, y)[y/x] = R(y, y), then [x/y] gives R(x, x); the swap through z
R = At('R', x, y)
assert sub(R, y, 'x') == At('R', y, y) and sub2(R, y, 'x', x, 'y') == At('R', x, x)
steps = [sub(R, z, 'x')]
steps.append(sub(steps[0], x, 'y')); steps.append(sub(steps[1], y, 'z'))
assert steps == [At('R', z, y), At('R', z, x), At('R', y, x)]
# Quick check: ((P(x) & Q(y))[y/x])[x/y]
phi = And(At('P', x), At('Q', y))
assert sub(phi, y, 'x') == And(At('P', y), At('Q', y))
assert sub2(phi, y, 'x', x, 'y') == And(At('P', x), At('Q', x))
assert sub(sub(sub(phi, z, 'x'), x, 'y'), y, 'z') == And(At('P', y), At('Q', x))
# Quick check after "Before you substitute": exists y (x < y) & P(y)
q = And(Ex('y', At('<', x, y)), At('P', y))
assert free_for(y, 'x', q) == QUOTED["QC2 y free for x"]
assert free_for(plus(x, C('1')), 'x', q) == QUOTED["QC2 x + 1 free for x"]
q2 = And(rename_top(Ex('y', At('<', x, y)), 'z'), At('P', y))
assert q2 == And(Ex('z', At('<', x, z)), At('P', y)) and free_for(y, 'x', q2)
assert sub(q2, y, 'x') == And(Ex('z', At('<', y, z)), At('P', y))
# (a)
fa = And(All('y', At('<', x, y)), Ex('x', Eq(x, y)))
assert fv(fa) == QUOTED["(a) FV"]
# (b)
assert (fv(All('x', Ex('y', Eq(plus(x, y), C('0'))))) == set()) == QUOTED["(b) sentence"]
# (c): (forall x P(x)) -> Q(x) has x free; the repair is a sentence
assert fv(Imp(All('x', At('P', x)), At('Q', x))) == QUOTED["(c) FV of the slip"]
assert fv(All('x', Imp(At('P', x), At('Q', x)))) == set()
# (d): x free as written; after the repair only a
absd = lambda s: F('abs', s)
inner = Imp(At('<', absd(F('-', x, a)), V('d')), At('<', absd(F('-', F('f', x), F('f', a))), V('e')))
bounded = lambda q, v, body: q(v, (Imp if q is All else And)(At('>', V(v), C('0')), body))
written = bounded(All, 'e', bounded(Ex, 'd', inner))
repaired = bounded(All, 'e', bounded(Ex, 'd', All('x', inner)))
assert fv(written) == {"x", "a"} and fv(repaired) == QUOTED["(d) FV after repair"]
# (e) (f) (g)
fe = And(At('<=', x, y), Ex('y', At('<', y, x)))
assert sub(fe, C('3'), 'x') == And(At('<=', C('3'), y), Ex('y', At('<', y, C('3'))))
assert sub(All('x', At('>=', x, y)), C('0'), 'y') == All('x', At('>=', x, C('0')))
fg = Imp(All('x', At('P', x)), At('P', x))
assert sub(fg, c, 'x') == Imp(All('x', At('P', x)), At('P', c))
# (h)
fh = Eq(plus(x, y), plus(y, x))
assert sub2(fh, y, 'x', x, 'y') == Eq(plus(x, x), plus(x, x))
swap = Eq(plus(y, x), plus(x, y))
assert (sub2(fh, y, 'x', x, 'y') == swap) == QUOTED["(h) swap?"]
# (i)
assert sub(At('P', x, y), F('f', y), 'x') == At('P', F('f', y), y)
assert sub2(At('P', x, y), F('f', y), 'x', c, 'y') == At('P', F('f', c), c)
# (j) (k) (l)
fj = Ex('x', At('>', x, y))
assert not free_for(x, 'y', fj)
assert free_for(plus(z, C('1')), 'y', fj) and sub(fj, plus(z, C('1')), 'y') == Ex('x', At('>', x, plus(z, C('1'))))
fl = rename_top(fj, 'z')
assert fl == Ex('z', At('>', z, y)) and sub(fl, x, 'y') == Ex('z', At('>', z, x))
print("exr-terms-formulas-substitution-a2: all quoted values check")
