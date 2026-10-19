"""def-truth-table and Section 3.3's tables: every printed truth table is evaluated cell by
cell (and its rows checked to be all 2^n rows in the book's order); the count of rows for
four atoms; the two readings of p and q or r at p = F, q = F, r = T (def-truth-value).
Deepening (Section 4.4): the Quick check on not p or (q <-> bot); the twelve parts of the
A2 drill (exr-valuations-and-truth-tables-a2); the truth-functional Quick check and drill
(l) (neither-nor, not-both); the game run at not (p and q)."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

SEC = "src/ch04-semantics-soundness-completeness/04-valuations-and-truth-tables.md"
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

P = L.parse
V = L.val
# Quick check: v(p) = T, v(q) = F
assert V(P(r"\neg p \vee (q \leftrightarrow \bot)"), {"p": True, "q": False}) is True
# A2 drill
v = {"p": True, "q": False}
assert V(P(r"p \to q"), v) is False                          # (a)
assert V(P(r"\neg p \to q"), v) is True                     # (b)
assert V(P(r"\bot \leftrightarrow q"), v) is True           # (c)
assert len(list(L.rows("pqrst"))) == 32                       # (d)
# (e) only v(p) = T known: value fixed whatever q, r are?
def fixed(s):
    vals = {V(P(s), {"p": True, "q": q, "r": r}) for q in (True, False) for r in (True, False)}
    return vals.pop() if len(vals) == 1 else None
assert fixed(r"p \vee q") is True and fixed(r"q \to p") is True
assert fixed(r"\neg p \to r") is True and fixed(r"p \wedge q") is None
assert [L.tv(r, "p", "q") for r in L.false_rows(r"(p \vee q) \to (p \wedge q)")] == \
    [(True, False), (False, True)]                            # (f)
assert [r["p"] for r in L.rows("p") if V(P(r"p \to \neg p"), r)] == [False]   # (g)
assert [L.tv(r, "p", "q", "r") for r in L.false_rows(r"p \to (q \to r)")] == \
    [(True, True, False)]                                     # (h)
assert [L.tv(r, "p", "q", "r") for r in L.rows("pqr") if V(P(r"(p \vee q) \wedge \neg r"), r)] == \
    [(True, True, False), (True, False, False), (False, True, False)]   # (i)
assert not L.false_rows(r"(p \to p) \vee q")                # (j)
# truth functions: neither-nor and not-both
for a in (True, False):
    for b in (True, False):
        e = {"p_1": a, "p_2": b}
        assert V(P(r"\neg p_1 \wedge \neg p_2"), e) == (not a and not b)
        assert V(P(r"\neg(p_1 \wedge p_2)"), e) == (not (a and b))
# the game (k) and the text's run: the verifier of not(p and q) wins iff it is true
def ver(f, v):
    k = f[0]
    if k == "atom": return v[f[1]]
    if k == "not": return fal(f[1], v)
    if k == "&": return ver(f[1], v) and ver(f[2], v)
    if k == "|": return ver(f[1], v) or ver(f[2], v)
def fal(f, v):
    k = f[0]
    if k == "atom": return not v[f[1]]
    if k == "not": return ver(f[1], v)
    if k == "&": return fal(f[1], v) or fal(f[2], v)
    if k == "|": return fal(f[1], v) and fal(f[2], v)
g = P(r"\neg(p \wedge q)")
for v in ({"p": True, "q": False}, {"p": False, "q": True}):
    assert ver(g, v) and V(g, v)
assert fal(P("q"), {"q": False}) and fal(P("p"), {"p": False})   # the conjunct chosen is false
print("def-truth-table: all quoted values check")
