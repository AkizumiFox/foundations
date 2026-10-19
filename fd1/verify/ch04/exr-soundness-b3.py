"""exr-soundness-b3 (Section 4.7, Derive or refute): the verdicts by truth table, the two
refuting rows, and the four derivations by tools/check_fitch.py on a capital-letter copy."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L
import _s0708_lib as H

claims = [([r"p \leftrightarrow q"], r"\neg p \leftrightarrow \neg q"),
          ([r"p \leftrightarrow \neg q"], r"\neg(p \wedge q)"),
          ([r"p \to q", r"q \to r"], r"r \to p"),
          ([r"\neg p \vee q"], r"p \to q"),
          ([r"p \leftrightarrow q", r"\neg q"], "p"),
          ([r"\neg(p \to q)"], r"q \to p")]
valid = [not L.entails(g, c) for g, c in claims]
assert valid == [True, True, False, True, False, True]
assert (False, False, True) in [L.tv(r, "p", "q", "r") for r in L.entails(*claims[2])]
assert (False, False) in [L.tv(r, "p", "q") for r in L.entails(*claims[4])]
# the look-alike of (e) holds; (f)'s premise is true in one row only, where q -> p is true
assert not L.entails([r"p \leftrightarrow q", r"\neg q"], r"\neg p")
rows_f = [r for r in L.rows(["p", "q"]) if L.val(L.parse(r"\neg(p \to q)"), r)]
assert len(rows_f) == 1 and L.val(L.parse(r"q \to p"), rows_f[0])
H.check(H.block(H.S07, "exr-soundness-b3"), derivations=4)
print("exr-soundness-b3: all quoted values check")
