"""exr-existential-introduction-a1 (Ch 4, Section 4.5): which of five lines follow from
R(c, f(c)) by one exists-I, with phi and t; the capture item over Z; the readings over N."""
from _s0102_fol import V, C, F, At, All, Eq, sub, free_for

QUOTED = {"legal": ["(i)", "(ii)", "(iii)"], "illegal": ["(iv)", "(v)"]}

x, y, c = V('x'), V('y'), C('c')
fc = F('f', c)
line = At('R', c, fc)
candidate_terms = [c, fc, x, y, C('d')]


def legal(phi):
    """Some term t with phi[t/x] equal to the line and t free for x in phi."""
    return [t for t in candidate_terms if sub(phi, t, 'x') == line and free_for(t, 'x', phi)]


cands = {"(i)": At('R', x, fc), "(ii)": At('R', c, x), "(iii)": At('R', x, F('f', x)),
         "(iv)": At('R', x, x), "(v)": At('R', fc, x)}
assert legal(cands["(i)"]) == [c] and legal(cands["(ii)"]) == [fc] and legal(cands["(iii)"]) == [c]
assert sorted(k for k, v in cands.items() if legal(v)) == QUOTED["legal"]
assert sorted(k for k, v in cands.items() if not legal(v)) == QUOTED["illegal"]
# (iv) R(t, t) can never be R(c, f(c)): the arguments of the line differ
assert c != fc
# readings over N with R as <, f(x) = x + 1, c = 0: line 0 < 1; (v) "something exceeds 1" true;
# (iv) "some number is less than itself" false
N = range(0, 200)
assert 0 < 0 + 1 and any(1 < d for d in N) and not any(d < d for d in N)

# (c): phi = forall y (y <= x * x); phi[y/x] is the line; y not free for x
xx = F('*', x, x)
phi = All('y', At('<=', y, xx))
assert sub(phi, y, 'x') == All('y', At('<=', y, F('*', y, y)))
assert not free_for(y, 'x', phi)
W = range(-200, 201)
assert all(d <= d * d for d in W)                         # line 1 true over Z
assert all(not (x0 * x0 + 1 <= x0 * x0) for x0 in W)      # y = x*x + 1 refutes every x
print("exr-existential-introduction-a1: all quoted values check")
