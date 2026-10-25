"""exr-countable-sets-b4: (a) f -> (f(0), f(1)) -> 2^a 3^b injective on functions {0,1} -> {0..30};
(c) A = {0} with the inclusion into N is injective and A is finite; (d) no function N -> empty set (no value at 0)."""
from itertools import product
R = range(31)
funcs = [{0: a, 1: b} for a, b in product(R, R)]
codes = [2 ** f[0] * 3 ** f[1] for f in funcs]
assert len(set(codes)) == len(funcs)
A = {0}
assert len({x for x in A}) == len(A) == 1
empty = set()
assert not any(True for _ in empty)  # nothing for f(0) to be
print("ok")
