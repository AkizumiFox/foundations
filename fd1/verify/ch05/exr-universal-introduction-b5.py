"""exr-universal-introduction-b5 (Section 5.4, derive or break: properties of a relation):
the counter-readings of (b), (d), (f) make every premise true and the conclusion false;
the "derive" claims (a), (c), (e) are true in every structure on a domain of size 1-3,
with f any function (a sanity check only; the derivations are checked by
tools/check_fitch.py)."""
import itertools
import sys
sys.path.insert(0, "verify/ch05")
from _fo_models import (structure, is_counter_model, all_relations, P, ALL, NOT, AND, IMP)

R = lambda s, t: P("R", s, t)
refl = ALL("x", R("x", "x"))
irrefl = ALL("x", NOT(R("x", "x")))
sym = ALL("x", ALL("y", IMP(R("x", "y"), R("y", "x"))))
asym = ALL("x", ALL("y", IMP(R("x", "y"), NOT(R("y", "x")))))
trans = ALL("x", ALL("y", ALL("z", IMP(AND(R("x", "y"), R("y", "z")), R("x", "z")))))
partner = ALL("x", R("x", ("f", "f", "x")))

CLAIMS = {
    "a": ([asym], irrefl),
    "b": ([irrefl], asym),
    "c": ([irrefl, trans], asym),
    "d": ([sym, trans], refl),
    "e": ([sym, trans, partner], refl),
    "f": ([refl], sym),
}
QUOTED = {
    "b": {(0, 1), (1, 0)},
    "d": {(0, 0)},
    "f": {(0, 0), (1, 1), (0, 1)},
}
for k, rel in QUOTED.items():
    prem, concl = CLAIMS[k]
    assert is_counter_model(prem, concl, structure([0, 1], pred={"R": rel})), k

for k in "ace":
    prem, concl = CLAIMS[k]
    for n in (1, 2, 3):
        D = list(range(n))
        fns = [dict(zip(D, v)).get for v in itertools.product(D, repeat=n)] if k == "e" else [None]
        for rel in all_relations(D, 2):
            for fn in fns:
                M = structure(D, func={"f": fn} if fn else {}, pred={"R": rel})
                assert not is_counter_model(prem, concl, M), (k, n)
print("exr-universal-introduction-b5: all quoted values check")
