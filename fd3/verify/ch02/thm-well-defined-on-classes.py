"""thm-well-defined-on-classes: the remark's witness. S = {(a, b) : 0 < a};
[(0, 0)] = [(1, 1)], (1, 1) in S, (0, 0) not in S."""
QUOTED = {"in_S": (1, 1), "not_in_S": (0, 0)}
rel = lambda p, q: p[0] + q[1] == p[1] + q[0]
S = lambda p: 0 < p[0]
assert rel(QUOTED["in_S"], QUOTED["not_in_S"])
assert S(QUOTED["in_S"]) and not S(QUOTED["not_in_S"])
print("thm-well-defined-on-classes: OK")
