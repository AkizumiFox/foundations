"""exr-axioms-or-model-r4: (10)^n >= 1 + 9n, the induction step
(1 + 9n) * 10 = 10 + 90n >= 10 + 9n = 1 + 9(n + 1), and 10^{-N} <= 1/N for N >= 1.
Linear identities are checked as coefficient lists (constant, coefficient of n)."""
from fractions import Fraction as Fr
QUOTED = {"step": ["10 + 90n", "10 + 9n", "1 + 9(n + 1)"]}
lhs = (1 * 10, 9 * 10)          # (1 + 9n) * 10
assert lhs == (10, 90)
assert (1 + 9, 9) == (10, 9)    # 1 + 9(n + 1) = 10 + 9n
for n in range(0, 300):
    assert 10 ** n >= 1 + 9 * n
    assert 10 + 90 * n >= 10 + 9 * n
    if n >= 1:
        assert 1 + 9 * n >= n and Fr(1, 10 ** n) <= Fr(1, n)
print("ok")
