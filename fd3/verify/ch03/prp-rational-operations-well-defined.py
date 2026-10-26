"""prp-rational-operations-well-defined (Section 3.1): the first-argument identities, the
symmetry g(y, x) = g(x, y) used for the second argument, negation, and the Quick check after
the proof ([(p, q)] + [(1, 1)] = [(p + q, q)]; (1, 3) not ~ (2, 5)). The second-argument
identities are kept as a cross-check (they are B2's solution). Each 'after substituting the hypothesis' step is checked by writing the hypothesis
as a difference: e.g. (ps + rq)(q's) - (p's + rq')(qs) = (pq' - p'q) s^2."""
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


p, q, r, s, p2, q2, r2, s2 = V("p q r s p2 q2 r2 s2")
# multiplication, first argument: (pr)(q's) - (p'r)(qs) = (pq' - p'q) rs
assert (p*r)*(q2*s) - (p2*r)*(q*s) == (p*q2 - p2*q)*(r*s)
assert (p*r)*(q2*s) == (p*q2)*(r*s) and (p2*q)*(r*s) == (p2*r)*(q*s)
# multiplication, second argument
assert (p*r)*(q*s2) - (p*r2)*(q*s) == (p*q)*(r*s2 - r2*s)
assert (p*r)*(q*s2) == (p*q)*(r*s2) and (p*q)*(r2*s) == (p*r2)*(q*s)
# addition, first argument
assert (p*s + r*q)*(q2*s) == (p*q2)*s*s + r*q*q2*s
assert (p2*s + r*q2)*(q*s) == (p2*q)*s*s + r*q*q2*s
assert (p*s + r*q)*(q2*s) - (p2*s + r*q2)*(q*s) == (p*q2 - p2*q)*s*s
# addition, second argument
assert (p*s + r*q)*(q*s2) == p*q*s*s2 + (r*s2)*q*q
assert (p*s2 + r2*q)*(q*s) == p*q*s*s2 + (r2*s)*q*q
assert (p*s + r*q)*(q*s2) - (p*s2 + r2*q)*(q*s) == (r*s2 - r2*s)*q*q
# negation
assert (-p)*q2 - (-p2)*q == -(p*q2 - p2*q)
# symmetry: g_+(y, x) = g_+(x, y) and g_.(y, x) = g_.(x, y) as pairs
gplus = lambda x, y: (x[0]*y[1] + y[0]*x[1], x[1]*y[1])
gdot = lambda x, y: (x[0]*y[0], x[1]*y[1])
X, Y = (p, q), (r, s)
assert gplus(Y, X) == gplus(X, Y) and gdot(Y, X) == gdot(X, Y)
# Quick check after the proof
one = (P.c(1), P.c(1))
assert gplus(X, one) == (p + q, q)
QUOTED = {"check_b": ((1, 3), (2, 5))}
a, b = QUOTED["check_b"]
assert (1 * 4 == 2 * 2) and a == (1, 2 + 1) and b == (2, 4 + 1) and a[0] * b[1] != b[0] * a[1]
print("prp-rational-operations-well-defined: all quoted values check")
