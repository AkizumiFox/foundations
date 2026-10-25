"""exr-infinite-sets-r3: number of truth functions with n inputs is 2^(2^n)."""
import itertools

QUOTED = {1: 4, 2: 16, 3: 256}

for n, count in QUOTED.items():
    rows = list(itertools.product("TF", repeat=n))
    assert len(rows) == 2**n
    funcs = set(itertools.product("TF", repeat=len(rows)))
    assert len(funcs) == count == 2 ** (2**n)
print("ok")
