"""prp-integers-embed-rationals (Section 10.4): j preserves +, ., -; [(p, 1)].[(1, q)] = [(p, q)];
[(q, 1)].[(1, q)] = 1."""
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


m, n, p, q = V("m n p q")


def add(x, y):
    return (x[0] * y[1] + y[0] * x[1], x[1] * y[1])


def mul(x, y):
    return (x[0] * y[0], x[1] * y[1])


def related(x, y):
    return x[0] * y[1] == y[0] * x[1]


j = lambda a: (a, P.c(1))
assert add(j(m), j(n)) == j(m + n)
assert mul(j(m), j(n)) == j(m * n)
assert (-m, P.c(1)) == j(-m)
assert mul(j(p), (P.c(1), q)) == (p, q)
assert related(mul(j(q), (P.c(1), q)), (P.c(1), P.c(1)))
print("prp-integers-embed-rationals: all quoted values check")
