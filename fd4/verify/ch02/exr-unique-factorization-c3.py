"""exr-unique-factorization-c3: the illustrations 211 and 30031 = 59 * 509."""
from math import prod

def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))

QUOTED = {"N4": 211, "N6": 30031, "f6": (59, 509), "new6": 59}
assert prod((2, 3, 5, 7)) + 1 == QUOTED["N4"] and is_prime(QUOTED["N4"])
assert prod((2, 3, 5, 7, 11, 13)) + 1 == QUOTED["N6"] == prod(QUOTED["f6"])
assert all(is_prime(p) for p in QUOTED["f6"]) and not is_prime(QUOTED["N6"])
assert min(d for d in range(2, QUOTED["N6"] + 1) if QUOTED["N6"] % d == 0) == QUOTED["new6"]
assert prod(()) + 1 == 2
print("exr-unique-factorization-c3: ok")
