"""exr-limits-c2: a_0 = 5, a_n = 0 (n >= 1), limit 0, N = 1 is legitimate for eps = 1,
yet |a_0| = 5 is not < 1 + |0|; the repaired bound max{|a_0|, |a| + 1} = 5 works."""
QUOTED = {"a0": 5, "N": 1, "bad_M": 1, "good_M": 5}
a = lambda k: QUOTED["a0"] if k == 0 else 0
assert all(abs(a(k) - 0) < 1 for k in range(QUOTED["N"], 100))
assert not (abs(a(0)) < 1 + abs(0)) and abs(a(0)) > QUOTED["bad_M"]
M = max([abs(a(k)) for k in range(QUOTED["N"])] + [abs(0) + 1])
assert M == QUOTED["good_M"] and all(abs(a(k)) <= M for k in range(100))
print("ok")
