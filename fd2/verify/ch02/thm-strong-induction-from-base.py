"""thm-strong-induction-from-base (Ch 7, 02): the Quick check: every n >= 24 is 5a + 7b (a, b >= 0);
the step n = (n - 5) + 5 needs the five base cases 24..28 with the quoted representations;
23 is the largest integer not of the form (23 - 7b = 23, 16, 9, 2 for b = 0..3)."""
QUOTED = {24: (2, 2), 25: (5, 0), 26: (1, 3), 27: (4, 1), 28: (0, 4)}
LARGEST_FAILURE = 23

def rep(n, x=5, y=7):
    return any((n - y * b) >= 0 and (n - y * b) % x == 0 for b in range(n // y + 1))

for n, (a, b) in QUOTED.items():
    assert 5 * a + 7 * b == n and a >= 0 and b >= 0
assert sorted(QUOTED) == [n for n in range(24, 29)]          # n - 5 >= 24 iff n >= 29
assert all(rep(n) for n in range(24, 500))
assert not rep(LARGEST_FAILURE) and max(n for n in range(0, 500) if not rep(n)) == LARGEST_FAILURE
assert [23 - 7 * b for b in range(4)] == [23, 16, 9, 2]
print("thm-strong-induction-from-base: all quoted values check")
