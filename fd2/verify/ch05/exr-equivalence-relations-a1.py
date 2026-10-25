"""exr-equivalence-relations-a1: (b) 7-4 = 3, 7-10 = -3, 4-10 = -6 = (-2)*3;
(c) on {1,2,3} with <=, [2] = {1,2}, [1] = {1}; (e) x^2 = y^2 on {-2..2} has 3 classes."""

QUOTED = {"b": (3, -3, -6, -2), "c2": {1, 2}, "c1": {1}, "e": 3}

assert (7 - 4, 7 - 10, 4 - 10, (4 - 10) // 3) == QUOTED["b"]
X = [1, 2, 3]
assert {x for x in X if x <= 2} == QUOTED["c2"] and {x for x in X if x <= 1} == QUOTED["c1"]
Y = range(-2, 3)
classes = {frozenset(x for x in Y if x * x == a * a) for a in Y}
assert len(classes) == QUOTED["e"]
assert classes == {frozenset({0}), frozenset({-1, 1}), frozenset({-2, 2})}
print("exr-equivalence-relations-a1: all quoted values check")
