"""exm-ill-defined-class-map: [0]_6 = [6]_6 but [0]_4 != [6]_4 = [2]_4; [a]_6 -> [a]_3 is well
defined (checked on representatives 0..59)."""

QUOTED = {"six_mod4": 2}

assert (6 - 0) % 6 == 0
assert 6 % 4 == QUOTED["six_mod4"] and (0 - 6) % 4 != 0
reps = range(0, 60)
assert all((a - b) % 3 == 0 for a in reps for b in reps if (a - b) % 6 == 0)
assert any((a - b) % 4 != 0 for a in reps for b in reps if (a - b) % 6 == 0)
print("exm-ill-defined-class-map: all quoted values check")
