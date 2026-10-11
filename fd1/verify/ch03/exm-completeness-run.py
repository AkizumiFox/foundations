"""exm-completeness-run (Section 3.6): (p->q) or (q->p) is a tautology; the method's derivation
has 20 lines with correct row citations; three splittings; the search derivation of
exr-finding-derivations-c2 has 13 lines."""
from pathlib import Path
from _s0607_lib import S06, ROOT, block, tautology, check_rows_in, count_lines, derivations

QUOTED = {"lines": 20, "chapter 2 lines": 13, "splittings": "Three uses"}
t = block(S06, "exm-completeness-run")
assert tautology("(p \\to q) \\vee (q \\to p)")
assert count_lines(t) == 20
assert check_rows_in(t) == 4
assert t.count("\\lem{}") == 3  # one split on p, two on q
c2 = block(ROOT / "src/ch02-negation-and-classical-logic/06-finding-derivations.md",
           "exr-finding-derivations-c2", stop="{#exr-finding-derivations-c3")
assert count_lines(c2) == 13
print("exm-completeness-run: all quoted values check")
