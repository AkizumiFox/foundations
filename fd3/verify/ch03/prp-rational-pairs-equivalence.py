"""prp-rational-pairs-equivalence (Section 10.4): the transitivity chain, and the failure of
transitivity on Z x N through (0, 0): (1, 0) ~ (0, 0) ~ (1, 1) but not (1, 0) ~ (1, 1)."""
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


from itertools import product
p, q, r, s, t, u = V("p q r s t u")
# with ps = rq and ru = ts substituted step by step, (pu)s = (ps)u = (rq)u = (ru)q = (ts)q = (tq)s
assert (p*u)*s == (p*s)*u and (r*q)*u == (r*u)*q and (t*s)*q == (t*q)*s
assert (p*u - t*q)*s == (p*u)*s - (t*q)*s
rel = lambda x, y: x[0] * y[1] == y[0] * x[1]
QUOTED = {"triple": ((1, 0), (0, 0), (1, 1))}
x, y, z = QUOTED["triple"]
assert rel(x, y) and rel(y, z) and not rel(x, z)
# brute-force check of (Eq1)-(Eq3) on a window of Z x Z_{>0}
W = [(a, b) for a in range(-4, 5) for b in range(1, 5)]
for x in W:
    assert rel(x, x)
for x, y in product(W, repeat=2):
    if rel(x, y):
        assert rel(y, x)
for x, y, z in product(W, repeat=3):
    if rel(x, y) and rel(y, z):
        assert rel(x, z)
print("prp-rational-pairs-equivalence: all quoted values check")
