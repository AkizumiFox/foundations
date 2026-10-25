"""exm-five-strings-diagonal: on the 1.5 list 00000, 11111, 01010, 10101, 00111 the diagonal
is 0, 1, 0, 0, 1 and the flip g = 10110 differs from s_k in place k; the rule works on every
5-list drawn from the 32 strings (exhaustive over random samples); 1.5's check answer 10010
is not the diagonal string. Quick check: a 32-list can contain every string."""
import itertools, random

QUOTED = {"list": ["00000", "11111", "01010", "10101", "00111"], "diag": "0, 1, 0, 0, 1", "g": "10110"}

def flip_diag(lst):
    return "".join(str(1 - int(s[k])) for k, s in enumerate(lst))

lst = QUOTED["list"]
assert ", ".join(s[k] for k, s in enumerate(lst)) == QUOTED["diag"]
g = flip_diag(lst)
assert g == QUOTED["g"] and g not in lst
for k, s in enumerate(lst):
    assert g[k] != s[k]
assert g != "10010"
strings = ["".join(t) for t in itertools.product("01", repeat=5)]
assert len(strings) == 32
random.seed(1)
for _ in range(20000):
    L = [random.choice(strings) for _ in range(5)]
    assert flip_diag(L) not in L
print("exm-five-strings-diagonal: all quoted values check")
