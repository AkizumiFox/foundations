"""exm-free-and-bound-limit (Ch 4, Section 4.2): only L is free in the unfolded limit formula."""
from _s0102_fol import *

QUOTED = {"only free variable": True}

e, N, n, L = V('eps'), V('N'), V('n'), V('L')
inner = All('n', Imp(At('inN', n), Imp(At('>=', n, N), At('<', F('abs', F('-', F('a', n), L)), e))))
lim = All('eps', Imp(At('>', e, C('0')), Ex('N', And(At('inN', N), inner))))
assert fv(lim) == {'L'}
# "take N = n": n is not free for N in the matrix psi
assert not free_for(n, 'N', inner)
assert sub(inner, n, 'N') == All('n', Imp(At('inN', n), Imp(At('>=', n, n), At('<', F('abs', F('-', F('a', n), L)), e))))
# eps/2 is free for eps in the matrix of the hypothesis
matrix = Imp(At('>', e, C('0')), Ex('N', And(At('inN', N), inner)))
assert free_for(F('/', e, C('2')), 'eps', matrix)
print("exm-free-and-bound-limit: all quoted values check")
