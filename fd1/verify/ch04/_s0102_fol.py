"""Tiny first-order syntax for the Ch 4 Sections 4.1-4.2 sidecars: terms, formulas,
free variables, substitution phi[t/x] exactly as def-substitution, free-for as def-free-for,
and renaming of bound variables."""

def V(x): return ('var', x)
def C(c): return ('const', c)
def F(f, *ts): return ('fn', f, tuple(ts))
def At(r, *ts): return ('atom', r, tuple(ts))
def Eq(s, t): return ('eq', s, t)
def Not(p): return ('not', p)
def And(p, q): return ('bin', 'and', p, q)
def Imp(p, q): return ('bin', 'imp', p, q)
def All(x, p): return ('all', x, p)
def Ex(x, p): return ('ex', x, p)
BOT = ('bot',)


def tvars(t):
    if t[0] == 'var':
        return {t[1]}
    if t[0] == 'const':
        return set()
    return set().union(*[tvars(s) for s in t[2]]) if t[2] else set()


def fv(p):
    k = p[0]
    if k == 'atom':
        return set().union(*[tvars(s) for s in p[2]])
    if k == 'eq':
        return tvars(p[1]) | tvars(p[2])
    if k == 'bot':
        return set()
    if k == 'not':
        return fv(p[1])
    if k == 'bin':
        return fv(p[2]) | fv(p[3])
    return fv(p[2]) - {p[1]}


def occurs(x, p):
    """x occurs anywhere in p, free, bound, or after a quantifier."""
    k = p[0]
    if k == 'atom':
        return any(x in tvars(s) for s in p[2])
    if k == 'eq':
        return x in tvars(p[1]) | tvars(p[2])
    if k == 'bot':
        return False
    if k == 'not':
        return occurs(x, p[1])
    if k == 'bin':
        return occurs(x, p[2]) or occurs(x, p[3])
    return p[1] == x or occurs(x, p[2])


def tsub(s, t, x):
    if s[0] == 'var':
        return t if s[1] == x else s
    if s[0] == 'const':
        return s
    return ('fn', s[1], tuple(tsub(u, t, x) for u in s[2]))


def sub(p, t, x):
    k = p[0]
    if k == 'atom':
        return ('atom', p[1], tuple(tsub(s, t, x) for s in p[2]))
    if k == 'eq':
        return ('eq', tsub(p[1], t, x), tsub(p[2], t, x))
    if k == 'bot':
        return p
    if k == 'not':
        return ('not', sub(p[1], t, x))
    if k == 'bin':
        return ('bin', p[1], sub(p[2], t, x), sub(p[3], t, x))
    if p[1] == x:
        return p
    return (k, p[1], sub(p[2], t, x))


def free_for(t, x, p, above=frozenset()):
    """def-free-for, read literally: no free occurrence of x lies in the scope of a
    quantifier on a variable of t.  `above` = variables quantified above this node."""
    k = p[0]
    if k in ('atom', 'eq'):
        terms = p[2] if k == 'atom' else (p[1], p[2])
        has_x = any(x in tvars(s) for s in terms)
        if has_x and x not in above:          # a free occurrence of x
            return not (tvars(t) & above)
        return True
    if k == 'bot':
        return True
    if k == 'not':
        return free_for(t, x, p[1], above)
    if k == 'bin':
        return free_for(t, x, p[2], above) and free_for(t, x, p[3], above)
    return free_for(t, x, p[2], above | {p[1]})


def free_for_rec(t, x, p):
    """The recursive description of 'free for' in the text."""
    k = p[0]
    if k in ('atom', 'eq', 'bot'):
        return True
    if k == 'not':
        return free_for_rec(t, x, p[1])
    if k == 'bin':
        return free_for_rec(t, x, p[2]) and free_for_rec(t, x, p[3])
    return (x not in fv(p)) or (p[1] not in tvars(t) and free_for_rec(t, x, p[2]))


def rename_top(p, z):
    """forall y phi  ->  forall z phi[z/y], z not occurring in phi."""
    assert p[0] in ('all', 'ex') and not occurs(z, p[2])
    return (p[0], z, sub(p[2], V(z), p[1]))


def shape(p):
    """Tree shape with quantifier kinds and binding structure, letters forgotten."""
    def go(q, env):
        k = q[0]
        def term(s):
            if s[0] == 'var':
                return ('b', env.index(s[1])) if s[1] in env else ('f', s[1])
            if s[0] == 'const':
                return s
            return ('fn', s[1], tuple(term(u) for u in s[2]))
        if k == 'atom':
            return ('atom', q[1], tuple(term(s) for s in q[2]))
        if k == 'eq':
            return ('eq', term(q[1]), term(q[2]))
        if k == 'bot':
            return q
        if k == 'not':
            return ('not', go(q[1], env))
        if k == 'bin':
            return ('bin', q[1], go(q[2], env), go(q[3], env))
        return (k, go(q[2], [q[1]] + env))
    return go(p, [])
