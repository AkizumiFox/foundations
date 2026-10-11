"""thm-integers-ordered-ring (Section 10.3): the product identity ac + bd = (ad + bc) + kl for
a = b + k, c = d + l; sums of positive classes; (a) iota(n) - iota(m) = [(n, m)]; and the
'two minimal changes' paragraph after the theorem (checked on sample integers)."""
# --- exact multivariate polynomials over Z (self-contained; no CAS needed) ---
class P:
    """Polynomial with integer coefficients: dict {sorted tuple of variable names: coeff}."""
    def __init__(self, terms=None):
        self.t = {k: v for k, v in (terms or {}).items() if v != 0}

    @staticmethod
    def c(n):
        return P({(): n})

    @staticmethod
    def v(name):
        return P({(name,): 1})

    @staticmethod
    def _lift(x):
        return x if isinstance(x, P) else P.c(x)

    def __add__(self, o):
        o = P._lift(o)
        r = dict(self.t)
        for k, v in o.t.items():
            r[k] = r.get(k, 0) + v
        return P(r)
    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.t.items()})

    def __sub__(self, o):
        return self + (-P._lift(o))

    def __rsub__(self, o):
        return P._lift(o) - self

    def __mul__(self, o):
        o = P._lift(o)
        r = {}
        for k1, v1 in self.t.items():
            for k2, v2 in o.t.items():
                k = tuple(sorted(k1 + k2))
                r[k] = r.get(k, 0) + v1 * v2
        return P(r)
    __rmul__ = __mul__

    def __eq__(self, o):
        return self.t == P._lift(o).t

    def __hash__(self):
        return hash(frozenset(self.t.items()))

    def __repr__(self):
        return " + ".join(f"{v}*{'*'.join(k) or '1'}" for k, v in sorted(self.t.items())) or "0"


def V(names):
    return [P.v(n) for n in names.split()]
# --- end of polynomial helper ---


b, d, k, l, m, n = V("b d k l m n")
a, c = b + k, d + l
assert a*c + b*d == (a*d + b*c) + k*l
assert a*c + b*d == b*d + b*l + k*d + k*l + b*d
assert a*d + b*c == b*d + k*d + b*d + b*l
# sums: (a + c) - (b + d) = k + l, nonzero when k, l are
assert (a + c) - (b + d) == k + l
# (a): [(n, 0)] + [(0, m)] = [(n, m)]
assert (n + 0, P.c(0) + m) == (n, m)

# 'two minimal changes', on the integers -5..5
R = range(-5, 6)
le = lambda u, v: u <= v
# <= breaks (O1) but keeps (O3), (O4)
assert le(0, 0) and 0 == 0          # both '0 <= 0' and '0 = 0' hold: (O1) fails
assert all(le(u + w, v + w) for u in R for v in R for w in R if le(u, v))       # (O3)
assert all(le(0, u * v) for u in R for v in R if le(0, u) and le(0, v))         # (O4)
# reversed order breaks (O4): 0 prec -1, (-1)(-1) = 1, not 0 prec 1
prec = lambda u, v: v < u
assert all(prec(u + w, v + w) for u in R for v in R for w in R if prec(u, v))   # (O3)
assert prec(0, -1) and (-1) * (-1) == 1 and not prec(0, 1)
QUOTED = {"warning_lhs": 9, "warning_rhs": 1}
assert (-3) * (-3) == QUOTED["warning_lhs"] and (-1) * (-1) == QUOTED["warning_rhs"]
print("thm-integers-ordered-ring: all quoted values check")
