"""exr-ordered-rings-b1 (Section 10.3): rows (F9), (F4), (F6) in detail."""
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


a, b, c, d, e, f = V("a b c d e f")
assert a*(c + e) + b*(d + f) == a*c + a*e + b*d + b*f
assert a*(d + f) + b*(c + e) == a*d + a*f + b*c + b*e
assert (a*c + b*d) + (a*e + b*f) == a*c + a*e + b*d + b*f
assert (a*d + b*c) + (a*f + b*e) == a*d + a*f + b*c + b*e
assert (a + b) + 0 == (b + a) + 0
assert (c*a + d*b, c*b + d*a) == (a*c + b*d, a*d + b*c)
print("exr-ordered-rings-b1: all quoted values check")
