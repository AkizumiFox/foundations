"""thm-am-gm (03): (a) product <= A^n for non-negative reals, (b) equality iff all equal;
the step identity 1 + (n+1)x = a_{n+1}/A_n with x = A_{n+1}/A_n - 1; the hook
((a+b)/2)^2 - ab = ((a-b)/2)^2; the warning (-1,-1,1): product 1, mean -1/3, A^3 = -1/27."""
from fractions import Fraction as Fr
import itertools, random
QUOTED = {"warning": ((-1, -1, 1), 1, Fr(-1, 3), Fr(-1, 27))}
def prod(xs):
    p = Fr(1)
    for x in xs:
        p *= x
    return p
lst, P, A, A3 = QUOTED["warning"]
assert prod(lst) == P and Fr(sum(lst), 3) == A and A ** 3 == A3 and A3 < P
for a in range(-5, 6):
    for b in range(-5, 6):
        assert Fr(a + b, 2) ** 2 - a * b == Fr(a - b, 2) ** 2
random.seed(2)
for _ in range(4000):
    n = random.randint(1, 6)
    xs = [Fr(random.randint(0, 6), random.randint(1, 3)) for _ in range(n)]
    A = sum(xs) / n
    if len(set(xs)) == 1:
        assert prod(xs) == A ** n
    else:
        assert prod(xs) < A ** n
    if all(x > 0 for x in xs) and n >= 2:
        m = n - 1
        Am, An = sum(xs[:m]) / m, sum(xs) / n
        x = An / Am - 1
        assert x > -1
        assert n * An == m * Am + xs[-1]
        assert 1 + n * x == xs[-1] / Am
        assert (1 + x) ** n * Am ** n == An ** n
        assert Am ** n * xs[-1] / Am == Am ** m * xs[-1]
        assert prod(xs) <= Am ** m * xs[-1] <= An ** n
print("ok")
