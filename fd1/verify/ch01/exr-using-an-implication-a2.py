"""exr-using-an-implication-a2 (Section 1.3, drill (j)): the form "if 6 | n then 3 | n;
3 | n; so 6 | n" is broken at n = 3."""
QUOTED = {"n": 3}
n = QUOTED["n"]
assert all(m % 3 == 0 for m in range(-6000, 6001) if m % 6 == 0)   # first premise, every n
assert n % 3 == 0 and n % 6 != 0
print("exr-using-an-implication-a2: checks")
