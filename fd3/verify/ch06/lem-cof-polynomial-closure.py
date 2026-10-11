"""lem-cof-polynomial-closure: the product list has length d + e + 1 and last entry a_d b_e
(for arbitrary lists, via the induction r = b_0 + t r'); the shifted list of t p(t);
and exm-cof-shift-automorphism: p(t + 1) has a list with the same top degree and top coefficient.
Also exm-cof-x-not-square / B3: t q^2 and (t^3 + 1) q^2 have odd top degree 2e + 1, 2e + 3."""
from fractions import Fraction as F
import random
QUOTED = {"top_degrees": ["2e + 1", "2e + 3"]}
def add(a, b):
    n = max(len(a), len(b)); a = a + [0] * (n - len(a)); b = b + [0] * (n - len(b))
    return [x + y for x, y in zip(a, b)]
def scal(c, a): return [c * x for x in a]
def shift(a): return [0] + a
def mul(a, b):  # the induction of the proof: r = b0 + t r'
    if len(b) == 1: return scal(b[0], a)
    return add(scal(b[0], a), shift(mul(a, b[1:])))
def ev(a, t): return sum(c * t ** i for i, c in enumerate(a))
def plus1(a):  # p(t+1) by p(t) = a0 + t p'(t)
    if len(a) == 1: return list(a)
    return add([a[0]], mul([1, 1], plus1(a[1:])))
def cut(a):
    while len(a) > 1 and a[-1] == 0: a = a[:-1]
    return a
random.seed(2)
for _ in range(2000):
    a = [random.randint(-5, 5) for _ in range(random.randint(1, 5))]
    b = [random.randint(-5, 5) for _ in range(random.randint(1, 5))]
    c = mul(a, b)
    assert len(c) == len(a) + len(b) - 1 and c[-1] == a[-1] * b[-1]
    for t in [F(-3), F(1, 2), F(7)]:
        assert ev(c, t) == ev(a, t) * ev(b, t)
        assert ev(add(a, b), t) == ev(a, t) + ev(b, t)
        assert ev(plus1(a), t) == ev(a, t + 1)
    s = plus1(a)
    assert len(s) == len(a) and s[-1] == a[-1]
    q = cut([random.randint(-5, 5) for _ in range(random.randint(1, 4))] + [random.choice([1, -2, 3])])
    e = len(q) - 1
    tq2 = mul([0, 1], mul(q, q)); assert len(tq2) - 1 == 2 * e + 1 and tq2[-1] == q[-1] ** 2
    cq2 = mul([1, 0, 0, 1], mul(q, q)); assert len(cq2) - 1 == 2 * e + 3 and cq2[-1] == q[-1] ** 2
print("ok")
