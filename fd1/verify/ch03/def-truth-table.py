"""def-truth-table and Section 3.3's tables: every printed truth table is evaluated cell by
cell (and its rows checked to be all 2^n rows in the book's order); the count of rows for
four atoms; the two readings of p and q or r at p = F, q = F, r = T (def-truth-value)."""
import sys
sys.path.insert(0, "verify/ch03")
import _logic as L

SEC = "src/ch03-semantics-soundness-completeness/03-valuations-and-truth-tables.md"
QUOTED = {"rows for four atoms": 16, "rows for three atoms": 8, "rows for five atoms": 32}

assert L.check_tables(SEC, expected_count=10) == 10
assert len(list(L.rows("pqrs"))) == QUOTED["rows for four atoms"]
assert len(list(L.rows("pqr"))) == QUOTED["rows for three atoms"]
assert len(list(L.rows("pqrst"))) == QUOTED["rows for five atoms"]
v = {"p": False, "q": False, "r": True}
assert L.val(L.parse(r"(p \wedge q) \vee r"), v) is True
assert L.val(L.parse(r"p \wedge (q \vee r)"), v) is False
# no-atom formulas have one value: not-bot is T, bot -> bot is T
assert L.val(L.parse(r"\neg\bot"), {}) and L.val(L.parse(r"\bot \to \bot"), {})
print("def-truth-table: all quoted values check")
