"""exr-rationals-as-classes-b1 (Section 10.4): rows (F9), (F4), (F2) in detail."""
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


p, q, r, s, t, u = V("p q r s t u")
assert p*(r*u + t*s) == p*r*u + p*t*s
A, B = p*r*u + p*t*s, q*s*u
assert (p*r)*(q*u) + (p*t)*(q*s) == q*A and (q*s)*(q*u) == q*B
assert A*(q*B) == (q*A)*B
assert p*q + (-p)*q == 0
assert (p*s + r*q)*u + t*(q*s) == p*s*u + q*r*u + q*s*t
assert p*(s*u) + (r*u + t*s)*q == p*s*u + q*r*u + q*s*t
print("exr-rationals-as-classes-b1: all quoted values check")
