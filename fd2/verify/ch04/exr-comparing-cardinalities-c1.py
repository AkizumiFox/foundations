"""exr-comparing-cardinalities-c1: y_S lies in [0.1, 0.3]; E(x) recovers the digits."""
from fractions import Fraction as F
import itertools

QUOTED = {"upper": F(3, 10), "lower": F(1, 10)}

# truncations of 0.e1e2... with digits in {1, 2}: t_n <= y <= t_n + 10^-n
for digits in itertools.product((1, 2), repeat=8):
    t = [sum(F(d, 10**(k + 1)) for k, d in enumerate(digits[:n])) for n in range(1, 9)]
    lo = t[-1]
    hi = min(t[n - 1] + F(1, 10**n) for n in range(1, 9))
    assert QUOTED["lower"] <= lo and hi <= QUOTED["upper"]
    assert t[0] + F(1, 10) <= QUOTED["upper"]
# E(x) = {10k + d_k}: quotient and remainder by 10 recover (k, d_k)
for digits in itertools.product(range(10), repeat=4):
    E = {10 * k + d for k, d in enumerate(digits, start=1)}
    back = {e // 10: e % 10 for e in E}
    assert back == {k: d for k, d in enumerate(digits, start=1)}
print("ok")
