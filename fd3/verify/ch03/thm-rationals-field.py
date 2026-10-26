"""thm-rationals-field (Section 10.4): every row of the field table ('equal' or 'related'), the
scaling observation, the inverses in (F8), and the Quick check after the theorem."""
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


from fractions import Fraction
p, q, r, s, t, u, k = V("p q r s t u k")


def add(x, y):
    return (x[0] * y[1] + y[0] * x[1], x[1] * y[1])


def mul(x, y):
    return (x[0] * y[0], x[1] * y[1])


def neg(x):
    return (-x[0], x[1])


def related(x, y):
    return x[0] * y[1] == y[0] * x[1]


x, y, z = (p, q), (r, s), (t, u)
ZERO, ONE = (P.c(0), P.c(1)), (P.c(1), P.c(1))
QUOTED = {"F1": "equal", "F2": "equal", "F3": "equal", "F4": "related", "F5": "equal",
          "F6": "equal", "F7": "equal", "F9": "related",
          "check_sum": (5, 6), "check_inverse": (-4, 3), "check_product": (12, 12)}
rows = {
    "F1": (add(x, y), add(y, x)), "F2": (add(add(x, y), z), add(x, add(y, z))),
    "F3": (add(x, ZERO), x), "F4": (add(x, neg(x)), ZERO),
    "F5": (mul(mul(x, y), z), mul(x, mul(y, z))), "F6": (mul(x, y), mul(y, x)),
    "F7": (mul(x, ONE), x), "F9": (mul(x, add(y, z)), add(mul(x, y), mul(x, z))),
}
for name, (l, rr) in rows.items():
    kind = "equal" if l == rr else ("related" if related(l, rr) else "fails")
    assert kind == QUOTED[name], (name, kind)
# pairs as displayed
assert add(add(x, y), z)[0] == p*s*u + q*r*u + q*s*t
assert add(x, neg(x)) == (P.c(0), q*q)
L, Rt = rows["F9"]
assert Rt == (q * L[0], q * L[1])
# scaling observation
assert related((p, q), (k * p, k * q))
# (F8): inverses
assert related(mul((p, q), (q, p)), ONE)
assert related(mul((p, q), (-q, -p)), ONE)
assert mul((p, q), (-q, -p)) == (-(p*q), -(p*q))
# Quick check
assert add((1, 2), (1, 3)) == QUOTED["check_sum"]
assert mul((-3, 4), QUOTED["check_inverse"]) == QUOTED["check_product"]
assert Fraction(-3, 4) * Fraction(-4, 3) == 1
print("thm-rationals-field: all quoted values check")
