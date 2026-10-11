"""prp-ordered-ring-rules (Section 10.3): the warning after it, the Quick check 'Is Z a field?',
the identity (a + b)^2 = a^2 + 2ab + b^2 of prp-ring-algebra (d), and the multiples n.a."""
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


a, b = V("a b")
assert (a + b) * (a + b) == a*a + 2*a*b + b*b
QUOTED = {"warning": ((-3, -1), (-3, -1), 9, 1)}
(a1, b1), (c1, d1), p1, p2 = QUOTED["warning"]
assert a1 < b1 and c1 < d1 and a1 * c1 == p1 and b1 * d1 == p2 and p1 > p2
# Quick check: 2x = 1 has no integer solution (search a window; the text proves it)
assert all(2 * x != 1 for x in range(-1000, 1001))


def mult(n, x, plus, zero):
    """n.a by the recursion 0.a = 0, (n + 1).a = n.a + a."""
    r = zero
    for _ in range(n):
        r = plus(r, x)
    return r


for n in range(0, 12):
    for x in range(-6, 7):
        assert mult(n, x, lambda u, v: u + v, 0) == n * x     # in Z the two readings agree
for m in range(0, 6):
    for k in range(0, 6):
        assert mult(m + k, 3, lambda u, v: u + v, 0) == mult(m, 3, lambda u, v: u + v, 0) + mult(k, 3, lambda u, v: u + v, 0)
print("prp-ordered-ring-rules: all quoted values check")
