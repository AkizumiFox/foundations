"""exm-sup-not-attained: hook values, the witness 1/eps, Quick check 2 (section 8.3)."""
from fractions import Fraction as Fr

QUOTED = {
    "hook": {0: Fr(0), 1: Fr(1, 2), 9: Fr(9, 10), 99: Fr(99, 100)},
    "qc2_x": Fr(1, 2), "qc2_value": Fr(1, 3), "qc2_bound": Fr(-1),
}

f = lambda x: Fr(x) / (1 + Fr(x))
for x, v in QUOTED["hook"].items():
    assert f(x) == v and v < 1

eps_list = [Fr(1, 1000), Fr(1, 10), Fr(1, 2), Fr(1), Fr(2), Fr(7, 3), Fr(100)]
for eps in eps_list:
    x = 1 / eps
    assert f(x) == 1 / (1 + eps)                        # value at the witness
    assert (1 - eps) * (1 + eps) == 1 - eps**2 < 1
    assert f(x) > 1 - eps                               # witness works, no case split
    assert f(x) - (1 - eps) == eps**2 / (1 + eps)
    if eps < 1:                                         # scratch work: x > 1/eps - 1 iff f(x) > 1 - eps
        for t in [1 / eps - 1 - Fr(1, 7), 1 / eps - 1, 1 / eps - 1 + Fr(1, 7)]:
            if t >= 0:
                assert (f(t) > 1 - eps) == (t > 1 / eps - 1)

eps = Fr(2)
assert 1 / eps == QUOTED["qc2_x"] and f(QUOTED["qc2_x"]) == QUOTED["qc2_value"]
assert 1 - eps == QUOTED["qc2_bound"] and QUOTED["qc2_value"] > QUOTED["qc2_bound"]
print("ok")
