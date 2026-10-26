"""thm-rationals-gap-sqrt2: the four identities of eq-newton-identities on many rationals s > 0;
the clearing-denominator computations quoted; t(s) < s and t(s)^2 > 2 when s^2 > 2; u(s) > s
and u(s)^2 < 2 when s^2 < 2; 2 bounds A (x > 2 gives x^2 > 4)."""
from fractions import Fraction as F
QUOTED = {}
t = lambda s: (s*s + 2) / (2*s)
u = lambda s: 4*s / (s*s + 2)
S = [F(a, b) for a in range(1, 60) for b in range(1, 30)]
for s in S:
    assert t(s)**2 - 2 == (s*s - 2)**2 / (4*s*s)
    assert s - t(s) == (s*s - 2) / (2*s)
    assert u(s) - s == s*(2 - s*s) / (s*s + 2)
    assert 2 - u(s)**2 == 2*(s*s - 2)**2 / (s*s + 2)**2
    assert u(s) == 2 / t(s)
    # cleared forms
    assert 4*s*s*(t(s)**2 - 2) == (s*s + 2)**2 - 8*s*s == s**4 - 4*s*s + 4 == (s*s - 2)**2
    assert 2*s*(s - t(s)) == 2*s*s - (s*s + 2) == s*s - 2
    assert (s*s + 2)*(u(s) - s) == 4*s - s**3 - 2*s == s*(2 - s*s)
    assert (s*s + 2)**2*(2 - u(s)**2) == 2*(s*s + 2)**2 - 16*s*s == 2*(s*s - 2)**2
    assert t(s) > 0 and u(s) > 0
    if s*s > 2:
        assert t(s) < s and t(s)**2 > 2
    if s*s < 2:
        assert u(s) > s and u(s)**2 < 2
for x in S:
    if x > 2:
        assert x*x > 4 > 2
print("ok")
