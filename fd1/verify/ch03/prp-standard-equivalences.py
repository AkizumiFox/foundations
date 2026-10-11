"""prp-standard-equivalences (Section 3.4): every printed table in the section is evaluated
(the tables of the proof, with phi, psi, chi as input columns, and B2's table); each
equivalence checked for atoms; long conjunctions/disjunctions and n-term De Morgan for
n <= 4; the Quick check on currying and grouping."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

SEC = "src/ch03-semantics-soundness-completeness/04-entailment-and-equivalence.md"
QUOTED = {"tables": 5}
assert L.check_tables(SEC, expected_count=5) == QUOTED["tables"]
pairs = [
    (r"p \to q", r"\neg q \to \neg p"),
    (r"\neg(p \wedge q)", r"\neg p \vee \neg q"),
    (r"\neg(p \vee q)", r"\neg p \wedge \neg q"),
    (r"p \to q", r"\neg p \vee q"),
    (r"\neg\neg p", r"p"),
    (r"p \leftrightarrow q", r"(p \to q) \wedge (q \to p)"),
    (r"p \wedge q", r"q \wedge p"), (r"p \vee q", r"q \vee p"),
    (r"p \wedge (q \vee r)", r"(p \wedge q) \vee (p \wedge r)"),
    (r"p \vee (q \wedge r)", r"(p \vee q) \wedge (p \vee r)"),
    (r"(p \wedge q) \wedge r", r"p \wedge (q \wedge r)"),
    (r"(p \vee q) \vee r", r"p \vee (q \vee r)"),
]
for a, b in pairs:
    assert L.equivalent(a, b), (a, b)
# long conjunctions, right-grouped, n <= 4
for n in range(1, 5):
    names = ["p_%d" % i for i in range(1, n + 1)]
    conj = " \\wedge ".join(names)
    disj = " \\vee ".join(names)
    for r in L.rows(names):
        assert L.val(L.parse(conj), r) == all(r.values())
        assert L.val(L.parse(disj), r) == any(r.values())
    assert L.equivalent("\\neg(" + conj + ")", " \\vee ".join("\\neg " + x for x in names))
    assert L.equivalent("\\neg(" + disj + ")", " \\wedge ".join("\\neg " + x for x in names))
# Quick check
assert L.equivalent(r"p \to (q \to r)", r"(p \wedge q) \to r")
assert not L.equivalent(r"p \to (q \to r)", r"(p \to q) \to r")
print("prp-standard-equivalences: all quoted values check")
