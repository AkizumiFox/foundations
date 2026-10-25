"""exr-functions-b3 (Ch 6 Section 6.4): s(0) = 0, s(n) = n - 1; t(n) = n + 1 (N = {0, 1, ...})."""

QUOTED = {"s(0) = s(1)": 0}

s = lambda n: 0 if n == 0 else n - 1
assert s(0) == s(1) == QUOTED["s(0) = s(1)"]
assert all(s(m + 1) == m for m in range(0, 200)) and all(s(n) >= 0 for n in range(0, 200))
t = lambda n: n + 1
assert all(t(n) >= 1 for n in range(0, 200))
print("exr-functions-b3: all quoted values check")
