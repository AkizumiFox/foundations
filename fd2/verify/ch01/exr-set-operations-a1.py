"""exr-set-operations-a1 (b): Z minus (2Z union 3Z) = odd non-multiples of 3."""
QUOTED = {"in both": (1, 5, -1, 7), "in neither": (3, 4, 6)}
lhs = lambda n: not (n % 2 == 0 or n % 3 == 0)
rhs = lambda n: (n % 2 != 0) and (n % 3 != 0)
assert all(lhs(n) == rhs(n) for n in range(-300, 301))
assert all(lhs(n) and rhs(n) for n in QUOTED["in both"])
assert all(not lhs(n) and not rhs(n) for n in QUOTED["in neither"])
print("exr-set-operations-a1: all quoted values check")
