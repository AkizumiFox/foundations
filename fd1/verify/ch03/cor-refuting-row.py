"""cor-refuting-row and the examples after it (Section 3.5): the refuting rows quoted for
p -> q |/- q -> p, p -> q, q |/- p, not(p and q) |/- not p and |/- not q, the Quick check
p -> r |/- (p or q) -> r, the warnings (p -> q, p |= q; p refuted by all-F), and the
contexts of the prp-contrapositive derivation (each line entailed by its context)."""
import sys
sys.path.insert(0, "verify/ch03")
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
