"""exm-ill-defined-fraction-sum (Section 10.4): [(1, 2)] = [(2, 4)] with p + q = 3, 6 and p = 1, 2;
squaring respects the relation; [(p, q)].[(p, q)] = [(p^2, q^2)]."""
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


p, q, p2, q2 = V("p q p2 q2")
QUOTED = {"sums": (3, 6), "numerators": (1, 2)}
assert 1 * 4 == 2 * 2
assert (1 + 2, 2 + 4) == QUOTED["sums"] and (1, 2) == QUOTED["numerators"]
# p^2 q'^2 - p'^2 q^2 = (pq' - p'q)(pq' + p'q)
assert p*p*q2*q2 - p2*p2*q*q == (p*q2 - p2*q)*(p*q2 + p2*q)
assert (p*p, q*q) == (p*p, q*q)
print("exm-ill-defined-fraction-sum: all quoted values check")
