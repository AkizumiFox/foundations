"""exr-limits-of-first-order-logic-a2 (Section 7.6): sigma_2 is true exactly on structures with
at least 2 elements, sigma_3 (the Quick check) with at least 3, and the "at most two" sentence
exactly on structures with at most 2 elements; sizes 1-4. Also forall x not(S(x) = 0) fails in
a one-element structure."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, ALL, EX, NOT, AND, OR

eq = lambda a, b: ("eq", a, b)
s2 = EX("x", EX("y", NOT(eq("x", "y"))))
s3 = EX("x", EX("y", EX("z", AND(NOT(eq("x", "y")), AND(NOT(eq("x", "z")), NOT(eq("y", "z")))))))
atmost2 = ALL("x", ALL("y", ALL("z", OR(eq("x", "y"), OR(eq("x", "z"), eq("y", "z"))))))
for n in range(1, 5):
    M = structure(range(n))
    assert sat(s2, M, {}) == (n >= 2)
    assert sat(s3, M, {}) == (n >= 3)
    assert sat(atmost2, M, {}) == (n <= 2)
M1 = structure([0], const={"0": 0}, func={"S": lambda d: 0})
assert not sat(ALL("x", NOT(("eq", ("f", "S", "x"), ("c", "0")))), M1, {})
print("exr-limits-of-first-order-logic-a2: all quoted values check")
