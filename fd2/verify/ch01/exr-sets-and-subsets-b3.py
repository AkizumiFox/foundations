"""exr-sets-and-subsets-b3: the four pairs of sets."""
QUOTED = {"(d) first set": (-1, 0, 1), "(b)": (-2, 2)}
# (a) 2 is even but not a multiple of 4
assert 2 % 2 == 0 and 2 % 4 != 0
# (b)
assert all(x * x == 4 for x in QUOTED["(b)"]) and 4 - 4 == (2 - 2) * (2 + 2)
assert tuple(x for x in range(-50, 51) if x * x == 4) == QUOTED["(b)"]  # integer roots; the real ones are +-2 by (x-2)(x+2)
# (c) as sets of frozensets
E = frozenset()
assert {E, frozenset({E})} == {frozenset({E}), E, E}
# (d)
first = tuple(sorted(n for n in range(-50, 51) if n * n < 2))
second = tuple(n for n in range(0, 51) if n < 2)  # N = {0, 1, ...}
assert first == QUOTED["(d) first set"] and second == (0, 1)
assert -1 in first and -1 not in second
print("exr-sets-and-subsets-b3: all quoted values check")
