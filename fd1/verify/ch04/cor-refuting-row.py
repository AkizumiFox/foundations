"""cor-refuting-row and the examples after it (Section 3.5): the refuting rows quoted for
p -> q |/- q -> p, p -> q, q |/- p, not(p and q) |/- not p and |/- not q, the Quick check
p -> r |/- (p or q) -> r, the warnings (p -> q, p |= q; p refuted by all-F), and the
contexts of the prp-contrapositive derivation (each line entailed by its context)."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

QUOTED = {"quick check row (p, q, r)": "p = \\mathrm{F} \\), \\( q = \\mathrm{T} \\), \\( r = \\mathrm{F}"}


def rows_of(prem, concl, *names):
    return sorted(L.tv(r, *names) for r in L.entails(prem, concl))


assert rows_of([r"p \to q"], r"q \to p", "p", "q") == [(False, True)]
assert rows_of([r"p \to q", "q"], "p", "p", "q") == [(False, True)]
assert (True, False) in rows_of([r"\neg(p \wedge q)"], r"\neg p", "p", "q")
assert (False, True) in rows_of([r"\neg(p \wedge q)"], r"\neg q", "p", "q")
assert (False, True, False) in rows_of([r"p \to r"], r"(p \vee q) \to r", "p", "q", "r")
assert rows_of([r"p \to r"], r"(p \vee q) \to r", "p", "q", "r") == [(False, True, False)]
assert not L.entails([r"p \to q", "p"], "q")
assert L.entails([], "p") and not L.entails([], r"p \vee \neg p")
# contexts of the contrapositive derivation: Gamma_k |= phi_k for k = 1..7
ctx = {1: [r"p \to q"], 2: [r"p \to q", r"\neg q"], 3: [r"p \to q", r"\neg q", "p"],
       4: [r"p \to q", r"\neg q", "p"], 5: [r"p \to q", r"\neg q", "p"],
       6: [r"p \to q", r"\neg q"], 7: [r"p \to q"]}
line = {1: r"p \to q", 2: r"\neg q", 3: "p", 4: "q", 5: r"\bot", 6: r"\neg p", 7: r"\neg q \to \neg p"}
for k in ctx:
    assert not L.entails(ctx[k], line[k]), k
# line 3 alone is not entailed by the premise (the failed first attempt)
assert L.entails([r"p \to q"], "p")
# exm-soundness-run and A1(c): contexts entail their lines
assert not L.entails([r"p \vee q", "p"], r"q \vee p") and not L.entails([r"p \vee q"], r"q \vee p")
for c, f in [([r"\neg p"], r"\neg p"), ([r"\neg p", "p"], r"\bot"), ([r"\neg p", "p"], "q"),
             ([r"\neg p"], r"p \to q")]:
    assert not L.entails(c, f)
print("cor-refuting-row: all quoted values check")

# --- Section 4.7 deepening (ch04-deepen.md item 6-8, A2) ---
import _s0708_lib as H
# R3's new Quick check: p = q = T does not refute p -> q |- q; p = q = F does
assert rows_of([r"p \to q"], "q", "p", "q") == [(False, False)]
# Quick check on contexts: the lines with p in their context are 3, 4, 5
assert [k for k in ctx if "p" in ctx[k]] == [3, 4, 5]
# the meaning table's four wrong versions: the rows refute what they would license
assert (True, False) in rows_of([], r"p \to (p \wedge q)", "p", "q")
assert (False, True) in rows_of([r"p \vee q"], "p", "p", "q")
assert rows_of([], r"\neg p", "p") == [(True,)]
assert rows_of([r"\neg p"], "p", "p") == [(False,)]
# the four wrong derivations (printed with P, Q) fail exactly at their last line
assert H.invalid_lines(H.between(H.S07, "## Every rule, checked", "## Refuting with one row")) == [["3"], ["4"], ["2"], ["4"]]
# test the subgoal: p or q |/- q at (T, F); the De Morgan subgoals
assert (True, False) in rows_of([r"p \vee q"], "q", "p", "q")
assert (True, False) in rows_of([r"\neg(p \wedge q)"], r"\neg p", "p", "q")
assert (False, True) in rows_of([r"\neg(p \wedge q)"], r"\neg q", "p", "q")
# its Quick check: the context p -> q, not q, p is unsatisfiable, and q follows
assert not L.entails([r"p \to q", r"\neg q", "p"], r"\bot") and not L.entails([r"p \to q", "p"], "q")
# A2 (a)-(h), R3's drill
assert (False, True) in rows_of([r"p \vee q"], "p", "p", "q")
assert (False, True) in rows_of([r"p \to q", r"\neg p"], r"\neg q", "p", "q")
assert not L.val(L.parse(r"p \wedge q"), {"p": True, "q": False})
assert not L.entails(["p", r"p \to q"], "q")
assert rows_of([], r"p \vee q", "p", "q") == [(False, False)]
assert (True, False, True) in rows_of([r"p \to (q \vee r)"], r"p \to q", "p", "q", "r")
# A2 (i)-(l)
assert (True, False) in rows_of([r"p \vee q"], "q", "p", "q")
sat = [L.tv(r, "p", "q") for r in L.rows(["p", "q"])
       if L.val(L.parse(r"p \to q"), r) and L.val(L.parse(r"q \to \neg p"), r)]
assert (False, True) in sat and (False, False) in sat and len(sat) == 2
assert not L.entails([r"p \to q", r"q \to \neg p", "p"], r"\bot")   # with p: unsatisfiable
assert (True, False, False) in rows_of([r"(p \wedge q) \to r"], r"(p \to r) \wedge (q \to r)", "p", "q", "r")
# retroactive paragraph: affirming the consequent (above); B3 of 3.2 is checked in 4.6's sidecars
print("cor-refuting-row: Section 4.7 additions check")
