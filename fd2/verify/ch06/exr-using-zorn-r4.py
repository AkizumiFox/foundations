"""6.3 Exercise R1 (exr-using-zorn-r4): D = {2, ..., 30} under divisibility.
Maximal elements 16, ..., 30; no greatest element; no least element."""

QUOTED = {"first_maximal": 16, "last_maximal": 30}

D = range(2, 31)


def div(a, b):
    return b % a == 0


maximal = [n for n in D if not any(div(n, m) and m != n for m in D)]
assert maximal == list(range(QUOTED["first_maximal"], QUOTED["last_maximal"] + 1))
assert all((2 * n > 30) == (n in maximal) for n in D)
assert not any(all(div(d, g) for d in D) for g in D)  # no greatest
assert not any(all(div(l, d) for d in D) for l in D)  # no least
assert not div(16, 17) and not div(17, 16)
print("ok")
