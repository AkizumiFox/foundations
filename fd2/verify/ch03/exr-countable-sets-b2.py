"""exr-countable-sets-b2: the counterexample to the reversed parities: m=1, m'=0, n=n'=0 gives 2 and 1."""
QUOTED = {"left": 2, "right": 1}
m, mp, n, np_ = 1, 0, 0, 0
assert 2**(m - mp) * 3**n == QUOTED["left"] and 3**np_ == QUOTED["right"]
print("ok")
