"""exm-threes-and-fives (Ch 3, Section 3.2): every n >= 8 is 3a + 5b, and 7 is not."""
QUOTED = {"bound": 8, "base cases": (8, 9, 10)}


def rep(n):
    return any((n - 5 * b) >= 0 and (n - 5 * b) % 3 == 0 for b in range(n // 5 + 1))


assert all(rep(n) for n in range(8, 1000))
assert not rep(7)          # 8 is best possible
assert 8 == 3 + 5 and 9 == 3 * 3 and 10 == 5 * 2
print("exm-threes-and-fives: all quoted values check")
