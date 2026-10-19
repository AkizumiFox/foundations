"""exm-not-formulas, exm-formation-sequences, the build-up figure and the Quick checks around them
(Ch 4, Section 4.1): which strings are formulas, and the formation sequences quoted."""
from _s0102_formulas import tok, is_formula, is_atom, BINARY

QUOTED = {
    "length of p and -> q": "it has length \\( 4 \\)",
    "build-up figure": ["p", "q", r"\neg q", r"(p \wedge \neg q)", r"((p \wedge \neg q) \to p)"],
    "figure uses": {3: (2,), 4: (1, 3), 5: (4, 1)},
    "new fourth string": ["p", r"\neg p", "q", r"\bot", r"(q \to \bot)", r"(\neg p \vee (q \to \bot))"],
    "new fourth string uses": {2: (1,), 5: (3, 4), 6: (2, 5)},
    "quick check neg(p or bot)": ["p", r"\bot", r"(p \vee \bot)", r"\neg(p \vee \bot)"],
    "quick check uses": {3: (1, 2), 4: (3,)},
    "A1 (c)": ["p", "q", r"(p \vee q)", r"\neg(p \vee q)", r"((p \vee q) \wedge \neg(p \vee q))"],
    "A1 (c) uses": {4: (3,), 5: (3, 4)},
}


def uses(seq, i):
    """1-based indices of earlier entries from which entry i is built (None if it is not built)."""
    x = seq[i - 1]
    if len(x) == 1 and (x[0] == "bot" or is_atom(x[0])):
        return ()
    for j in range(1, i):
        if x == ("neg",) + seq[j - 1]:
            return (j,)
    for j in range(1, i):
        for l in range(1, i):
            for op in BINARY:
                if x == ("(",) + seq[j - 1] + (op,) + seq[l - 1] + (")",):
                    return (j, l)
    return None


def check_sequence(strings, used, complete=True):
    seq = [tok(s) for s in strings]
    for i in range(1, len(seq) + 1):
        u = uses(seq, i)
        assert u is not None, strings[i - 1]
        if i in used:
            assert set(u) == set(used[i]), (strings[i - 1], u)
        elif u and complete:
            raise AssertionError(("entry uses earlier entries but none quoted", strings[i - 1]))
    assert all(is_formula(x) for x in seq)


for s in [r"p \wedge \to q", r"(p \wedge q", r"(\neg p)", r"p \wedge q", r"(p \to \neg)", r"\bot\bot"]:
    assert not is_formula(tok(s)), s
for s in ["p", r"\bot", r"\neg\neg q", r"(\neg p \vee (q \to \bot))", r"\neg(p \to \bot)", r"(p \wedge q)"]:
    assert is_formula(tok(s)), s
assert len(tok(r"p \wedge \to q")) == 4
check_sequence(QUOTED["build-up figure"], QUOTED["figure uses"])
check_sequence(QUOTED["new fourth string"], QUOTED["new fourth string uses"])
check_sequence(["q", r"\neg q", r"\neg\neg q"], {2: (1,), 3: (2,)})
check_sequence(QUOTED["quick check neg(p or bot)"], QUOTED["quick check uses"])
check_sequence(QUOTED["A1 (c)"], QUOTED["A1 (c) uses"], complete=False)
# fold "Many formation sequences": q listed before p in the last list is still a formation sequence
check_sequence(["q", "p", r"\neg p", r"\bot", r"(q \to \bot)", r"(\neg p \vee (q \to \bot))"],
               {3: (2,), 5: (1, 4), 6: (3, 5)})
# the figure: p used twice (entries 4 and 5), listed once
fig = [tok(s) for s in QUOTED["build-up figure"]]
assert fig.count(("p",)) == 1 and tok(QUOTED["build-up figure"][-1]).count("p") == 2
print("exm-not-formulas: all quoted values check")
