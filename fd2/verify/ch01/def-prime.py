"""def-prime (Ch 7, 02): 2, 3, 7 are prime; 9 = 3 * 3 is not; 1 is excluded by p >= 2."""
def pos_divisors(p):
    return [d for d in range(1, p + 1) if p % d == 0]
for p in (2, 3, 7):
    assert pos_divisors(p) == [1, p]
assert 3 in pos_divisors(9) and 9 == 3 * 3
assert pos_divisors(1) == [1]
print("def-prime: all quoted values check")
