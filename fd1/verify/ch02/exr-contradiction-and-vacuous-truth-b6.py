"""exr-contradiction-and-vacuous-truth-b6 (Ch 2, Section 2.1), part (d): for n = 3, 6, 8, the truth
values of "n is a multiple of 4" and "n is even", and which paradox decides the implication:
not-P |- P -> Q needs P false; Q |- P -> Q needs Q true."""
QUOTED = {"n": (3, 6, 8)}
# (hypothesis true?, conclusion true?, which sequent decides the implication)
CASES = {3: (False, False, "first only"), 6: (False, True, "either"), 8: (True, True, "second only")}
assert tuple(CASES) == QUOTED["n"]
for n, (hyp, concl, which) in CASES.items():
    assert (n % 4 == 0) == hyp and (n % 2 == 0) == concl, n
    first, second = (not hyp), concl
    got = {(True, False): "first only", (True, True): "either",
           (False, True): "second only", (False, False): "neither"}[(first, second)]
    assert got == which, n
assert 8 == 4 * 2
print("exr-contradiction-and-vacuous-truth-b6: all quoted values check")
