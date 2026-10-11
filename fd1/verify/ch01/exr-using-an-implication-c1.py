"""exr-using-an-implication-c1 (Section 1.4): the premises are true and the conclusion false."""
QUOTED = {"10 = 2*5": (2, 5), "10 = 6*1 + 4": (6, 1, 4)}
assert all(m % 2 == 0 for m in range(-600, 601) if m % 6 == 0)   # every multiple of 6 is even
a, b = QUOTED["10 = 2*5"]; assert a * b == 10
d, q, r = QUOTED["10 = 6*1 + 4"]; assert d * q + r == 10 and 0 < r < d
assert 10 % 6 != 0
print("exr-using-an-implication-c1: checks")
