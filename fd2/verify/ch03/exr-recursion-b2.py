"""exr-recursion-b2: 2^n >= n^2 fails only at n = 3 in 0..60; base 16 >= 16; step valid iff n >= 3."""
QUOTED = {"fails": [3], "base": (16, 16), "P3": (8, 9)}
assert [n for n in range(61) if 2**n < n * n] == QUOTED["fails"]
assert (2**4, 4**2) == QUOTED["base"] and (2**3, 3**2) == QUOTED["P3"]
# 2n^2 >= (n+1)^2  <=>  (n-1)^2 - 2 >= 0 : true for n >= 3, false at n = 2
assert all((2 * n * n >= (n + 1) ** 2) == (n >= 3) for n in range(0, 200))
assert (2 - 1) ** 2 - 2 == -1 and all((n - 1) ** 2 >= 9 for n in range(4, 100))
print("ok")
