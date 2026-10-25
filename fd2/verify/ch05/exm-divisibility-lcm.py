"""exm-divisibility-lcm: L = 6 for a = 2, b = 3 (none of 1..5 is a common multiple); sup{4,6} = 12
under divisibility and 6 under <=; the least positive common multiple divides every integer common
multiple (checked for a, b in 1..12 and common multiples c in -200..200); sup{a, 0} = 0."""
from math import lcm

QUOTED = {"L23": 6, "sup46_div": 12, "sup46_le": 6}

def least_cm(a, b):
    return min(m for m in range(1, a * b + 1) if m % a == 0 and m % b == 0)

assert least_cm(2, 3) == QUOTED["L23"]
assert not any(m % 2 == 0 and m % 3 == 0 for m in range(1, 6))
assert least_cm(4, 6) == QUOTED["sup46_div"] and max(4, 6) == QUOTED["sup46_le"]
for a in range(1, 13):
    for b in range(1, 13):
        L = least_cm(a, b)
        assert L == lcm(a, b)
        assert all(c % L == 0 for c in range(-200, 201) if c % a == 0 and c % b == 0)
# upper bounds of {a, 0} in (N, |): c with a | c and 0 | c, i.e. c = 0
assert [c for c in range(0, 100) if c % 5 == 0 and c == 0] == [0]
print("exm-divisibility-lcm: all quoted values check")
