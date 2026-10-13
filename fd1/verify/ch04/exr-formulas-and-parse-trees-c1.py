"""exr-formulas-and-parse-trees-c1 (Ch 3, Section 3.1): groupings of p -> q -> r -> s."""
from _s0102_formulas import is_formula

QUOTED = {"c_3": 2, "c_4": 5, "c_11 (eleven atoms)": 16796}


def groupings(atoms):
    if len(atoms) == 1:
        return [(atoms[0],)]
    out = []
    for k in range(1, len(atoms)):
        for l in groupings(atoms[:k]):
            for r in groupings(atoms[k:]):
                out.append(("(",) + l + ("imp",) + r + (")",))
    return out


g4 = groupings(["p", "q", "r", "s"])
assert len(g4) == QUOTED["c_4"] and len(set(g4)) == 5 and all(is_formula(f) for f in g4)
assert len(groupings(["p", "q", "r"])) == QUOTED["c_3"]
c = [1, 1]  # c_1, c_2
for n in range(3, 12):
    c.append(sum(c[k - 1] * c[n - k - 1] for k in range(1, n)))
assert c[:4] == [1, 1, 2, 5] and c[5] == 42 and c[10] == QUOTED["c_11 (eleven atoms)"]
# rule 4 (right grouping) is the first formula listed
assert ("(", "p", "imp", "(", "q", "imp", "(", "r", "imp", "s", ")", ")", ")") in g4
print("exr-formulas-and-parse-trees-c1: all quoted values check")
