"""exr-using-an-implication-c1 (Section 1.3): the premises are true and the conclusion false."""
QUOTED = {"10 = 2*5": (2, 5), "6k <= 6 for k <= 1, 6k >= 12 for k >= 2": (6, 1, 12, 2)}
assert all(m % 2 == 0 for m in range(-600, 601) if m % 6 == 0)   # every multiple of 6 is even
a, b = QUOTED["10 = 2*5"]; assert a * b == 10
lo, k_lo, hi, k_hi = QUOTED["6k <= 6 for k <= 1, 6k >= 12 for k >= 2"]
assert k_hi == k_lo + 1 and lo == 6 * k_lo and hi == 6 * k_hi and lo < 10 < hi
assert 10 % 6 != 0
assert all(6 * k <= lo for k in range(-100, k_lo + 1)) and all(6 * k >= hi for k in range(k_hi, 100))   # 10 = 6k for no k
print("exr-using-an-implication-c1: checks")
