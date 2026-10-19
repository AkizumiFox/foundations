"""lem-lindenbaum (Section 4.10): the Quick check and B1 stages, and drill (f), with
'consistent' decided by truth table on the finite lists (soundness and completeness, 4.7-4.8);
the row v_Delta of B1."""
from _logic import parse, val, rows, atoms
def sat(fs):
    fs = [parse(f) for f in fs]
    names = sorted(set().union(*(atoms(f) for f in fs))) or ["p"]
    return any(all(val(f, r) for f in fs) for r in rows(names))
def run(gamma, lst):
    d = list(gamma)
    stages = []
    for f in lst:
        if sat(d + [f]):
            add = f
        else:
            add = "\\neg " + ("(" + f + ")" if " " in f and not f.startswith("\\neg") else f)
            assert sat(d + [add])           # the key step
        if add not in d:
            d.append(add)
        stages.append(list(d))
    return stages
G = ["p \\vee q", "\\neg p"]
s = run(G, ["p", "q", "\\neg q", "p \\wedge q"])
assert s[0] == G                                   # Delta_1 = Gamma (adds not p, already there)
assert s[1] == G + ["q"]
assert s[2] == G + ["q", "\\neg \\neg q"]
assert s[3] == G + ["q", "\\neg \\neg q", "\\neg (p \\wedge q)"]
# the row: p false, q true is the only row making Delta_4 true
good = [r for r in rows(["p", "q"]) if all(val(parse(f), r) for f in s[3])]
assert good == [{"p": False, "q": True}]
# drill (f)
s = run(["p"], ["q", "\\neg p"])
assert s[0] == ["p", "q"] and s[1] == ["p", "q", "\\neg \\neg p"]
print("lem-lindenbaum: all quoted values check")
