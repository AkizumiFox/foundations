"""exr-axioms-or-model-r3: the transfer facts use n * 1 = 2 and n * 1 = 3.
2 is not a rational square (small search), and 3 is not a square in Q(sqrt 2):
(a + b sqrt 2)^2 = (a^2 + 2 b^2) + 2ab sqrt 2, so 2ab = 0 and then a^2 = 3 or 2 b^2 = 3,
neither of which has a rational solution (small search). The four classes are
{Q}, {Q(sqrt 2)}, {R(x)}, {R, X}, told apart by (Archimedean, 2 a square, 3 a square)."""
from fractions import Fraction
QUOTED = {"n_two": 2, "n_three": 3}
two, three = QUOTED["n_two"], QUOTED["n_three"]
rats = {Fraction(p, q) for q in range(1, 60) for p in range(0, 200)}
assert not any(r * r == two for r in rats)                     # 2 not a square in Q
assert not any(r * r == three for r in rats)                   # a^2 = 3 (b = 0)
assert not any(2 * r * r == three for r in rats)               # 2 b^2 = 3 (a = 0)
# invariants: (Archimedean, 2 is a square, 3 is a square)
inv = {"Q": (True, False, False), "Q(sqrt2)": (True, True, False),
       "R(x)": (False, True, True), "R": (True, True, True), "X": (True, True, True)}
classes = {}
for k, v in inv.items():
    classes.setdefault(v, []).append(k)
assert len(classes) == 4 and sorted(classes[(True, True, True)]) == ["R", "X"]
print("ok")
