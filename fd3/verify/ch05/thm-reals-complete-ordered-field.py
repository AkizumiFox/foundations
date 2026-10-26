"""thm-reals-complete-ordered-field (Section 5.5), bisection with rational ends.
Quick check: A = {q in Q : q^2 < 2} from (l_0, u_0) = (0, 2): (l_k, u_k) = (0, 2), (1, 2), (1, 3/2), (5/4, 3/2);
D = 2, u_3 - l_3 = 1/4 = D/2^3; 7/5 in A (49/25 < 2); midpoints 1, 3/2, 5/4; 9/4 >= 2.
Proof, Steps 1-3 on finite sets A (exact rationals): Step 1's start (a_0 - 1 < l_0 < a_0, M < u_0 < M + 1);
invariants (I1)-(I3); eq-rational-bisection-tail; D/2^k < eps for k >= n once D/eps < n; l_k <= sup A <= u_k.
Exercise C1 (dyadic grid): m_k least in U_k, u_{k+1} <= u_k, u_k - 1/2^k not an upper bound,
u_k - 1/2^k < u_j <= u_k for j >= k; p + 1 in U_k and p' a lower bound (integer parts)."""
from fractions import Fraction as F
import math, random

QUOTED = {"pairs": [(F(0), F(2)), (F(1), F(2)), (F(1), F(3, 2)), (F(5, 4), F(3, 2))],
          "mid": [F(1), F(3, 2), F(5, 4)], "width3": F(1, 4), "D": 2}

# --- Quick check ---
def ub_sqrt2(c):
    # for c > 0: c is an upper bound of A iff c^2 >= 2 (no rational has square 2)
    return c > 0 and c * c >= 2
assert F(7, 5) ** 2 == F(49, 25) < 2 and F(3, 2) ** 2 == F(9, 4) >= 2
l, u = F(0), F(2)
pairs, mids = [(l, u)], []
for k in range(3):
    c = (l + u) / 2
    mids.append(c)
    if ub_sqrt2(c):
        u = c
    else:
        assert F(7, 5) > c   # the witness used in the text
        l = c
    pairs.append((l, u))
assert pairs == QUOTED["pairs"] and mids == QUOTED["mid"]
D = pairs[0][1] - pairs[0][0]
assert D == QUOTED["D"] and pairs[3][1] - pairs[3][0] == QUOTED["width3"] == D / 2 ** 3

# --- The proof on finite sets of rationals (sup = max) ---
def bisect(A, l0, u0, K):
    ub = lambda c: all(a <= c for a in A)
    assert not ub(l0) and ub(u0)
    D = u0 - l0
    ends = [(l0, u0)]
    l, u = l0, u0
    for k in range(K):
        assert ub(u) and not ub(l) and u - l == D / 2 ** k          # (I1)-(I3)
        c = (l + u) / 2
        l, u = (l, c) if ub(c) else (c, u)
        ends.append((l, u))
    return D, ends

random.seed(5)
for trial in range(200):
    A = [F(random.randint(-50, 50), random.randint(1, 9)) for _ in range(random.randint(1, 5))]
    a0, M = A[0], max(A) + F(random.randint(0, 5), 3)
    # Step 1: rationals strictly inside (a0 - 1, a0) and (M, M + 1)
    l0 = a0 - F(random.randint(1, 99), 100)
    u0 = M + F(random.randint(1, 99), 100)
    assert a0 - 1 < l0 < a0 and M < u0 < M + 1 and u0 - l0 > 0
    D, ends = bisect(A, l0, u0, 40)
    s = max(A)
    for k in range(len(ends)):
        lk, uk = ends[k]
        assert lk <= s <= uk                                       # l_k <= s <= u_k
        for j in range(k, len(ends)):
            lj, uj = ends[j]
            assert 0 <= uk - uj <= D / 2 ** k and 0 <= lj - lk <= D / 2 ** k   # tail display
    # Step 3: D/eps < n implies D/2^k < eps for k >= n
    eps = F(random.randint(1, 9), random.randint(1, 300))
    n = math.floor(D / eps) + 1
    assert D / eps < n
    for k in (n, n + 1, n + 7):
        assert 2 ** k >= k + 1 > n > D / eps and D / F(2 ** k) < eps

# --- Exercise C1: dyadic grid ---
def least_m(ub, k, a0, M, top):
    p = math.floor(2 ** k * M)          # integer part of 2^k M
    pp = math.floor(2 ** k * a0)        # integer part of 2^k a0: a lower bound of U_k
    assert ub(F(p + 1, 2 ** k))         # p + 1 in U_k
    m = math.ceil(2 ** k * top)         # candidate least element (top = max A)
    assert ub(F(m, 2 ** k)) and not ub(F(m - 1, 2 ** k)) and pp <= m <= p + 1
    return m

for A, a0, M in [([F(0), F(1)], F(0), F(1)), ([F(-7, 3), F(5, 6)], F(-7, 3), F(2)), ([F(1, 3)], F(1, 3), F(1, 3))]:
    ub = lambda c, A=A: all(a <= c for a in A)
    us = []
    for k in range(25):
        m = least_m(ub, k, a0, M, max(A))
        uk = F(m, 2 ** k)
        assert not ub(uk - F(1, 2 ** k))                           # u_k - 1/2^k not an upper bound
        us.append(uk)
    for k in range(len(us)):
        for j in range(k, len(us)):
            assert us[k] - F(1, 2 ** k) < us[j] <= us[k]
        assert us[k] - F(1, 2 ** k) < max(A) <= us[k]
# A = {q : q^2 < 2}: upper bounds c > 0 with c^2 >= 2
us = []
for k in range(30):
    m = math.isqrt(2 * 4 ** k - 1) + 1   # least m with m^2 >= 2 * 4^k
    assert ub_sqrt2(F(m, 2 ** k))
    us.append(F(m, 2 ** k))
    assert not ub_sqrt2(F(m - 1, 2 ** k))
for k in range(len(us) - 1):
    assert us[k + 1] <= us[k] and us[k] - us[k + 1] < F(1, 2 ** k)
print("ok")
