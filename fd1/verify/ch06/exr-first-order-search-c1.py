"""exr-first-order-search-c1 (Section 6.3): the skeleton p -> p is a tautology; on random
finite sequences, some index n has D(n) -> forall m D(m) (any index if all terms are
positive, an index with a_n <= 0 otherwise)."""
import random
from _tt import entails, imp
assert entails("p", [], lambda v: imp(v["p"], v["p"]))
random.seed(6)
for _ in range(2000):
    k = random.randint(1, 8)
    a = [random.choice([-2, -1, 0, 1, 2, 3]) for _ in range(k)]
    D = lambda n: a[n] > 0
    allD = all(D(m) for m in range(k))
    good = [n for n in range(k) if imp(D(n), allD)]
    assert good
    if allD:
        assert good == list(range(k))
    else:
        assert all(not D(n) for n in good)
print("exr-first-order-search-c1: all quoted values check")
