"""exr-polynomials-as-sequences-b1 (Section 4.1): the polynomials over F_2 with
p_k = 0 for k > 2, listed from the eight triples (a_0, a_1, a_2)."""
from itertools import product

QUOTED = {
    "list": ["0", "1", "x", "x + 1", "x^2", "x^2 + 1", "x^2 + x", "x^2 + x + 1"],
}


def display(t):
    terms = []
    for k in (2, 1, 0):
        if t[k]:
            terms.append({0: "1", 1: "x", 2: "x^2"}[k])
    return " + ".join(terms) if terms else "0"


listed = sorted(display(t) for t in product((0, 1), repeat=3))
assert len(set(listed)) == 8
assert listed == sorted(QUOTED["list"])
print("exr-polynomials-as-sequences-b1: ok")
