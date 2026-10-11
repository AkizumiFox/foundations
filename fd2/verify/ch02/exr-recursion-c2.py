"""exr-recursion-c2: x = -2 holds for all n; at x = -4 first failure n = 3, first failing step n = 2."""
QUOTED = {"first_fail": 3, "first_bad_step": 2, "values_x_minus_4": [(1, 1), (-3, -3), (9, -7), (-27, -11)]}
assert all((-1) ** n >= 1 - 2 * n for n in range(500))
P = lambda n: (1 - 4) ** n >= 1 + n * (-4)
assert [((-3) ** n, 1 - 4 * n) for n in range(4)] == QUOTED["values_x_minus_4"]
assert min(n for n in range(100) if not P(n)) == QUOTED["first_fail"]
assert min(n for n in range(100) if P(n) and not P(n + 1)) == QUOTED["first_bad_step"]
print("ok")
