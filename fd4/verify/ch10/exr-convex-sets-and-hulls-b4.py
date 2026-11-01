"""exr-convex-sets-and-hulls-b4: (e) lambda x + mu y = (lambda+mu)((1-s)x + s y), s = mu/(lambda+mu) in [0,1];
counterexample C = {0, e1}: e1 in C + C, not in 2C. (b) (+-2,0) outside closed unit ball, midpoint inside.
(d) ||x-p||^2 - ||x-q||^2 = 2<q-p,x> - (||q||^2 - ||p||^2) on random data."""
from fractions import Fraction as F
import random
QUOTED = {"s": "mu/(lambda+mu)", "counter": True}
random.seed(2)
for _ in range(2000):
    L, M = F(random.randint(0, 20)), F(random.randint(0, 20))
    X = [F(random.randint(-9, 9)) for _ in range(3)]; Y = [F(random.randint(-9, 9)) for _ in range(3)]
    if L + M > 0:
        S = M / (L + M); assert 0 <= S <= 1
        assert all((L + M) * ((1 - S) * x + S * y) == L * x + M * y for x, y in zip(X, Y))
C = {(0, 0), (1, 0)}
CC = {(a[0] + b[0], a[1] + b[1]) for a in C for b in C}
twoC = {(2 * a[0], 2 * a[1]) for a in C}
assert (1, 0) in CC and (1, 0) not in twoC
assert 2**2 > 1 and (-2)**2 > 1 and 0 <= 1
def dot(u, v): return sum(i * j for i, j in zip(u, v))
for _ in range(500):
    P = [F(random.randint(-9, 9)) for _ in range(3)]; Q = [F(random.randint(-9, 9)) for _ in range(3)]; X = [F(random.randint(-9, 9)) for _ in range(3)]
    d = lambda u, v: dot([a - b for a, b in zip(u, v)], [a - b for a, b in zip(u, v)])
    qp = [a - b for a, b in zip(Q, P)]
    assert d(X, P) - d(X, Q) == 2 * dot(qp, X) - (dot(Q, Q) - dot(P, P))
print("ok")
