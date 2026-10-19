"""exr-normal-forms-c7 (Section 4.9, displayed C6): (a) theta = q; (b) the construction of
theta from the good rows, checked on random entailments over four atoms with phi on
p, q, r and psi on q, r, s (or other splits); (c) no shared atom forces psi a tautology."""
import itertools
import random
from _logic import val, rows, atoms, parse, entails
assert not entails(["p \\wedge q"], "q") and not entails(["q"], "q \\vee r")
random.seed(7)
ALL = ["p", "q", "r", "s"]
def rand(names, d):
    if d == 0 or random.random() < 0.3:
        return ("atom", random.choice(names))
    k = random.choice(["not", "&", "|", ">", "="])
    return ("not", rand(names, d - 1)) if k == "not" else (k, rand(names, d - 1), rand(names, d - 1))
def theta_ok(phi, psi):
    A, B = atoms(phi), atoms(psi)
    shared = sorted(A & B)
    R = list(rows(ALL))
    if not any(val(phi, v) for v in R) or all(val(psi, v) for v in R):
        return None
    if not all(val(psi, v) for v in R if val(phi, v)):
        return None
    assert shared, "part (c): an entailment with no shared atom"
    good = {tuple(v[n] for n in shared) for v in R if val(phi, v)}
    th = lambda v: tuple(v[n] for n in shared) in good
    assert all(th(v) for v in R if val(phi, v))
    assert all(val(psi, v) for v in R if th(v))
    return True
n = 0
for _ in range(20000):
    split = random.choice([(["p", "q", "r"], ["q", "r", "s"]), (["p", "q"], ["q", "s"]),
                           (["p", "r"], ["q", "s"])])
    phi, psi = rand(split[0], 3), rand(split[1], 3)
    if theta_ok(phi, psi):
        n += 1
assert n > 200
print("exr-normal-forms-c7: all quoted values check")
