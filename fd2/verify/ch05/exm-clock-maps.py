"""exm-clock-maps, the warning after thm-functions-out-of-quotient, and the
[a]_10 -> [a]_5 Quick check.
(a) remainder mod 2 is constant on classes mod 12; r(0) = r(2) but 0, 2 differ mod 12.
(b) on Z/2 the induced map is a bijection.
(c) tick [a] -> [a+1] on Z/12 is well defined and a bijection with inverse [a] -> [a-1].
Warning: [a]_12 -> [a]_24: converse holds, but 0 = 12 mod 12 and [0]_24 != [12]_24.
Quick check: [a]_10 -> [a]_5 well defined, [0]_10 != [5]_10 same image, onto."""

QUOTED = {"r0": 0, "r1": 1, "r2": 0, "warn": (0, 12), "qc": (0, 5)}
R = range(-200, 201)


def const_on_classes(g, n):
    return all(g(a) == g(b) for a in R for b in R if (a - b) % n == 0)


r = lambda a: a % 2
assert (r(0), r(1), r(2)) == (QUOTED["r0"], QUOTED["r1"], QUOTED["r2"])
assert const_on_classes(r, 12)
assert (2 - 0) % 12 != 0
# (b) injective on Z/2: r(a) = r(b) => a = b mod 2
assert all((a - b) % 2 == 0 for a in R for b in R if r(a) == r(b))
# (c) tick
tick = lambda a: (a + 1) % 12
assert const_on_classes(tick, 12)
back = lambda a: (a - 1) % 12
assert all(back(tick(a)) == a % 12 and tick(back(a)) == a % 12 for a in R)
assert sorted(tick(a) for a in range(12)) == list(range(12))
# warning
g24 = lambda a: a % 24
assert all((a - b) % 12 == 0 for a in R for b in R if g24(a) == g24(b))
a, b = QUOTED["warn"]
assert (a - b) % 12 == 0 and g24(a) != g24(b)
assert not const_on_classes(g24, 12)
# quick check [a]_10 -> [a]_5
g5 = lambda a: a % 5
assert const_on_classes(g5, 10)
a, b = QUOTED["qc"]
assert g5(a) == g5(b) and (a - b) % 10 != 0
assert {g5(a) for a in range(10)} == set(range(5))
print("exm-clock-maps: all quoted values check")
