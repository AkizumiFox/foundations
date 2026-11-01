"""thm-sup-function-rules: the warning after (b), reused in exr-bounds-and-suprema-b2 (a) and -b4."""
from fractions import Fraction as Fr

QUOTED = {"sup_f": 1, "sup_g": 1, "sup_sum": 1, "sum_of_sups": 2, "b4_value": 2}
pts = [Fr(k, 200) for k in range(201)]
f = lambda x: x
g = lambda x: 1 - x
assert max(map(f, pts)) == QUOTED["sup_f"] == f(1)
assert max(map(g, pts)) == QUOTED["sup_g"] == g(0)
assert {f(x) + g(x) for x in pts} == {QUOTED["sup_sum"]}
assert QUOTED["sup_f"] + QUOTED["sup_g"] == QUOTED["sum_of_sups"]
assert f(1) + g(0) == QUOTED["b4_value"]
# rule (g) on a sample: |sup f - sup h| <= sup |f - h|
h = lambda x: x * x
assert abs(max(map(f, pts)) - max(map(h, pts))) <= max(abs(f(x) - h(x)) for x in pts)
print("ok")
