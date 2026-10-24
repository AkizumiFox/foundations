"""exr-first-order-search-c2 (Section 6.3): M(n) 'n is an even prime greater than 2' is empty
on 0..200, so both premises are vacuously true and 'some even number is odd' is false; the
skeleton of (b)'s TAUT line m, m -> p, m -> s |= s and p."""
from _tt import entails, imp


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n ** 0.5) + 1))


W = range(0, 201)
M = lambda n: n % 2 == 0 and prime(n) and n > 2
assert not any(M(n) for n in W)
assert all(imp(M(n), n % 2 == 1) for n in W) and all(imp(M(n), n % 2 == 0) for n in W)
assert not any(n % 2 == 0 and n % 2 == 1 for n in W)
assert entails("mps", [lambda v: v["m"], lambda v: imp(v["m"], v["p"]), lambda v: imp(v["m"], v["s"])],
               lambda v: v["s"] and v["p"])
print("exr-first-order-search-c2: all quoted values check")
