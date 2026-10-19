"""prp-more-equivalences (Section 4.9): the ten laws (a)-(e) by truth table, with phi, psi
read as atoms (the method of prp-standard-equivalences); the two printed tables' entries."""
from _logic import parse, val, rows, equivalent
LAWS = [
    ("\\varphi \\wedge \\neg\\bot", "\\varphi"), ("\\varphi \\vee \\bot", "\\varphi"),
    ("\\varphi \\wedge \\bot", "\\bot"), ("\\varphi \\vee \\neg\\bot", "\\neg\\bot"),
    ("\\varphi \\wedge \\neg\\varphi", "\\bot"), ("\\varphi \\vee \\neg\\varphi", "\\neg\\bot"),
    ("\\varphi \\wedge \\varphi", "\\varphi"), ("\\varphi \\vee \\varphi", "\\varphi"),
    ("\\varphi \\wedge (\\varphi \\vee \\psi)", "\\varphi"),
    ("\\varphi \\vee (\\varphi \\wedge \\psi)", "\\varphi"),
]
for l, r in LAWS:
    for env in rows(["PHI", "PSI"]):
        assert val(parse(l), env) == val(parse(r), env), (l, r)
# the first printed table: rows a = T, a = F; columns in the printed order
T1 = {True: "TTFTFTTT", False: "FFFTFTFF"}
for a, expect in T1.items():
    got = "".join("T" if val(parse(l), {"PHI": a, "PSI": True}) else "F" for l, _ in LAWS[:8])
    assert got == expect, (a, got)
T2 = {(True, True): "TT", (True, False): "TT", (False, True): "FF", (False, False): "FF"}
for (a, b), expect in T2.items():
    got = "".join("T" if val(parse(l), {"PHI": a, "PSI": b}) else "F" for l, _ in LAWS[8:])
    assert got == expect
QUOTED = {"laws": 10}
print("prp-more-equivalences: all quoted values check")
