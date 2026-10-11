"""exr-induction-in-practice-c1 (Ch 7, 02): representability by 4a + 7b for 0..60; 17 is the largest
failure; 18 = 4 + 7*2, 19 = 4*3 + 7, 20 = 4*5, 21 = 7*3; line (5) is out of range exactly for
n = 18, 19, 20; base 14: 14, 15, 16 representable, 13 and 17 not."""
QUOTED = {18: (1, 2), 19: (3, 1), 20: (5, 0), 21: (0, 3), 14: (0, 2), 15: (2, 1), 16: (4, 0)}

def rep(n):
    return any((n - 7 * b) >= 0 and (n - 7 * b) % 4 == 0 for b in range(n // 7 + 1))

for n, (a, b) in QUOTED.items():
    assert 4 * a + 7 * b == n
fails = [n for n in range(0, 61) if not rep(n)]
assert max(fails) == 17 and all(rep(n) for n in range(18, 61))
assert [n for n in range(18, 100) if n - 3 < 18] == [18, 19, 20]
assert not rep(13) and not rep(17)
assert [17 - 7 * b for b in range(3)] == [17, 10, 3]
print("exr-induction-in-practice-c1: all quoted values check")
