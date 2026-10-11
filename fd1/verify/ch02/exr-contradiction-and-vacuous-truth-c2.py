"""exr-contradiction-and-vacuous-truth-c2 (Ch 2, Section 2.1): the counterexample to the illegal step:
P = "x > 0", Q = "x = 7" at x = -1: the premise not P holds and the line Q fails."""
QUOTED = {"x": -1, "Q value": 7}

x = QUOTED["x"]
assert not (x > 0)          # premise not(x > 0) is true
assert x != QUOTED["Q value"]  # conclusion x = 7 is false
print("exr-contradiction-and-vacuous-truth-c2: all quoted values check")
