"""thm-cauchy-algebra-ordered-field (c): a_n b_n - a_m b_m = a_n (b_n - b_m) + b_m (a_n - a_m)
(a polynomial identity of degree 2, checked on many exact rational points);
the final bound A * eps/(2A) + B * eps/(2B) = eps."""
from fractions import Fraction as F
import itertools, random
QUOTED = {"identity": "a_n b_n - a_m b_m = a_n (b_n - b_m) + b_m (a_n - a_m)"}
random.seed(0)
r = lambda: F(random.randint(-60, 60), random.randint(1, 20))
for _ in range(5000):
    an, am, bn, bm = r(), r(), r(), r()
    assert an*bn - am*bm == an*(bn - bm) + bm*(an - am)
for _ in range(2000):
    A, B, eps = abs(r()) + F(1, 7), abs(r()) + F(1, 9), abs(r()) + F(1, 11)
    assert A*(eps/(2*A)) + B*(eps/(2*B)) == eps
print("ok")
