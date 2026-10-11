"""exm-rational-function-field and its uses (A1 (b), the reciprocal identity): leading-coefficient checks
with polynomials as coefficient lists (index = degree)."""
from fractions import Fraction as Fr

QUOTED = {"t_minus_n_lead": 1, "t2_minus_n_lead": 1, "nt_lead": "n"}

def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p

def add(p, q):
    n = max(len(p), len(q))
    return trim([(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)])

def mul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return trim(r)

def neg(p):
    return [-a for a in p]

def lead(p):
    return trim(p)[-1]

def positive(num, den):
    return lead(num) * lead(den) > 0

t = [Fr(0), Fr(1)]
for n in range(0, 50):
    c = [Fr(n)]
    assert lead(add(t, neg(c))) == QUOTED["t_minus_n_lead"] and positive(add(t, neg(c)), [Fr(1)])
    assert positive(add(add(t, [Fr(1)]), neg(c)), [Fr(1)])
    assert lead(add(mul(t, t), neg(c))) == QUOTED["t2_minus_n_lead"]
    if n >= 1:
        # 1/n - 1/t = (t - n)/(n t): cross-multiplied, (1*t - n*1) * (n t) == (t - n) * (n * t)
        lhs_num, lhs_den = add(mul([Fr(1)], t), neg(mul(c, [Fr(1)]))), mul(c, t)
        rhs_num, rhs_den = add(t, neg(c)), mul(c, t)
        assert mul(lhs_num, rhs_den) == mul(rhs_num, lhs_den)
        assert lead(rhs_den) == n > 0 and positive(rhs_num, rhs_den)
assert positive([Fr(1)], t)
print("ok")
