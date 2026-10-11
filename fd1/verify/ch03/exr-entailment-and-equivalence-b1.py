"""exr-entailment-and-equivalence-b1 (Section 3.4): verdicts and the refuting row of (c).
(The derivations of (a), (b), (d) are checked by tools/check_fitch.py on a capital-letter
copy.)"""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

QUOTED = {"valid": 3}
verdicts = [
    not L.entails([r"p \to q", r"\neg q"], r"\neg p"),
    not L.entails([r"p \to (q \vee r)", r"\neg q"], r"p \to r"),
    not L.entails([r"p \to q"], r"\neg p \to \neg q"),
    not L.entails([r"p \vee q", r"p \to r", r"q \to r"], "r"),
]
assert verdicts == [True, True, False, True] and sum(verdicts) == QUOTED["valid"]
assert [L.tv(r, "p", "q") for r in L.entails([r"p \to q"], r"\neg p \to \neg q")] == [(False, True)]
# B2
assert L.equivalent(r"p \leftrightarrow q", r"(p \wedge q) \vee (\neg p \wedge \neg q)")
print("exr-entailment-and-equivalence-b1: all quoted values check")
