"""thm-well-ordering (Ch 7, 01): the Quick check: the least n in N with n^2 > 50 is 8;
7^2 = 49, 8^2 = 64, 10^2 = 100, and n^2 <= 49 for n <= 7."""
QUOTED = {"least": 8, "7^2": 49, "8^2": 64, "10^2": 100, "max_sq_below": 49}

S = [n for n in range(0, 200) if n * n > 50]
assert min(S) == QUOTED["least"]
assert 7 ** 2 == QUOTED["7^2"] and 8 ** 2 == QUOTED["8^2"] and 10 ** 2 == QUOTED["10^2"]
assert max(n * n for n in range(0, 8)) == QUOTED["max_sq_below"] <= 50
assert 10 in S
print("thm-well-ordering: all quoted values check")
