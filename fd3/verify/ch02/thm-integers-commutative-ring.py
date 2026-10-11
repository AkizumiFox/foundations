"""thm-integers-commutative-ring (Section 10.3): every row of the axiom table, the (F5)
expansion written out below it, and 1 != 0. Integers are classes of pairs (a, b) of natural
numbers, (p, q) ~ (r, s) iff p + s = q + r. Pairs are compared as polynomials in a..f."""
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


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] + x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def neg(x):
    return (x[1], x[0])


def related(x, y):
    return x[0] + y[1] == x[1] + y[0]


x, y, z = (a, b), (c, d), (e, f)
ZERO, ONE = (P.c(0), P.c(0)), (P.c(1), P.c(0))

# kind of agreement claimed in the table: "equal" (same pair) or "related" (~ only)
QUOTED = {
    "F1": "equal", "F2": "equal", "F3": "equal", "F4": "related",
    "F5": "equal", "F6": "equal", "F7": "equal", "F9": "equal",
    "F5_first": [a*c*e, b*d*e, a*d*f, b*c*f],
    "F5_second": [a*c*f, b*d*f, a*d*e, b*c*e],
}
rows = {
    "F1": (add(x, y), add(y, x)),
    "F2": (add(add(x, y), z), add(x, add(y, z))),
    "F3": (add(x, ZERO), x),
    "F4": (add(x, neg(x)), ZERO),
    "F5": (mul(mul(x, y), z), mul(x, mul(y, z))),
    "F6": (mul(x, y), mul(y, x)),
    "F7": (mul(x, ONE), x),
    "F9": (mul(x, add(y, z)), add(mul(x, y), mul(x, z))),
}
for name, (l, r) in rows.items():
    kind = "equal" if l == r else ("related" if related(l, r) else "fails")
    assert kind == QUOTED[name], (name, kind)
# the pairs shown in the table
assert add(x, neg(x)) == (a + b, b + a)
assert mul(x, ONE) == (a * 1 + b * 0, a * 0 + b * 1)
assert mul(x, add(y, z)) == (a*(c + e) + b*(d + f), a*(d + f) + b*(c + e))
assert add(mul(x, y), mul(x, z)) == ((a*c + b*d) + (a*e + b*f), (a*d + b*c) + (a*f + b*e))
# (F5) written out: g = ac + bd, h = ad + bc
g, h = a*c + b*d, a*d + b*c
assert g*e + h*f == sum(QUOTED["F5_first"], P.c(0))
assert g*f + h*e == sum(QUOTED["F5_second"], P.c(0))
assert a*(c*e + d*f) + b*(c*f + d*e) == sum(QUOTED["F5_first"], P.c(0))
assert a*(c*f + d*e) + b*(c*e + d*f) == sum(QUOTED["F5_second"], P.c(0))
# 1 != 0: (1, 0) ~ (0, 0) would need 1 + 0 = 0 + 0
assert not (1 + 0 == 0 + 0)
# remark: iota(a) + (-iota(b)) = [(a, 0)] + [(0, b)] = [(a, b)]
assert add((a, P.c(0)), neg((b, P.c(0)))) == (a, b)
print("thm-integers-commutative-ring: all quoted values check")
