"""lem-connective-rows (Section 3.6): the fifteen sequents are valid; the "Rows covered"
column is right; the case choice used in lem-truth-table-line calls, for each connective and
pair of values, a row whose premises are the signed parts and whose conclusion is the signed
whole; the printed derivations have 4, 6, 7, 9, 6, 6 and 2 lines."""
from _s0607_lib import S06, ROWS, block, derivations, cf, value, rows, check_row_instance

QUOTED = {"lines (->2), (->3), (<->1), (<->2), (<->3), (<->4), (bot1)": [4, 6, 7, 9, 6, 6, 2]}

# every sequent is valid (as a schema: with atoms A, B it is valid, and substitution keeps it)
for tag, (prem, concl) in ROWS.items():
    ps = [cf.parse_formula(x) for x in prem]
    c = cf.parse_formula(concl)
    for env in rows("AB"):
        if all(value(p, env) for p in ps):
            assert value(c, env), tag

# the case choice of lem-truth-table-line
OPS = {"and": "\\wedge", "or": "\\vee", "imp": "{\\to}", "iff": "{\\leftrightarrow}"}
def choose(op, a, b):
    if op == "and":
        return "(\\wedge 1)" if a and b else ("(\\wedge 2)" if not a else "(\\wedge 3)")
    if op == "or":
        return "(\\vee 1)" if a else ("(\\vee 2)" if b else "(\\vee 3)")
    if op == "imp":
        return "({\\to}1)" if not a else ("({\\to}2)" if b else "({\\to}3)")
    return {(1, 1): "({\\leftrightarrow}1)", (0, 0): "({\\leftrightarrow}2)",
            (1, 0): "({\\leftrightarrow}3)", (0, 1): "({\\leftrightarrow}4)"}[(a, b)]
A, B = ("var", "A"), ("var", "B")
sign = lambda f, t: f if t else ("not", f)
for op in OPS:
    for a in (True, False):
        for b in (True, False):
            tag = choose(op, a, b)
            whole = (op, A, B)
            w = value(whole, {"A": a, "B": b})
            prem, _ = ROWS[tag]
            cited = []
            for x in prem:
                cited.append(sign(A, a) if "A" in x else sign(B, b))
            assert check_row_instance(tag, cited, sign(whole, w)), (op, a, b, tag)

# printed derivations: count lines, in the order of the text
txt = block(S06, "lem-connective-rows", stop="None of these derivations uses")
ds = derivations(txt)
counts = [len(o) for o, _ in ds]
assert counts == QUOTED[list(QUOTED)[0]], counts
# and none uses RAA
assert "\\raa" not in txt
print("lem-connective-rows: all quoted values check")
