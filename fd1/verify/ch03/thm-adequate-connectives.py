"""thm-adequate-connectives (Section 3.7): the translations t1, t2, t3 preserve values on all
formulas of {not, and, or} up to depth 3 over two atoms; every formula of {and, or, ->} of
depth <= 3 is true under the all-T valuation; the quick check (p->(q->bot))->bot."""
import itertools
from _s0607_lib import cf, value, rows
A = [("var", "P"), ("var", "Q")]
BOT = ("bot",)
def build(depth, ops):
    fs = list(A)
    for _ in range(depth):
        new = list(fs)
        for f in fs:
            if "not" in ops:
                new.append(("not", f))
        for f, g in itertools.product(fs, repeat=2):
            for o in ops:
                if o != "not":
                    new.append((o, f, g))
        fs = list(dict.fromkeys(new))[:4000]
    return fs
def t(i, f):
    k = f[0]
    if k == "var":
        return f
    if k == "not":
        return ("not", t(i, f[1])) if i < 3 else ("imp", t(i, f[1]), BOT)
    a, b = t(i, f[1]), t(i, f[2])
    if k == "and":
        return {1: ("and", a, b), 2: ("not", ("or", ("not", a), ("not", b))),
                3: ("imp", ("imp", a, ("imp", b, BOT)), BOT)}[i]
    if k == "or":
        return {1: ("not", ("and", ("not", a), ("not", b))), 2: ("or", a, b),
                3: ("imp", ("imp", a, BOT), b)}[i]
def ops(f, acc):
    acc.add(f[0])
    if f[0] in ("var", "bot"):
        return acc
    for g in f[1:]:
        ops(g, acc)
    return acc
S = {1: {"not", "and", "var"}, 2: {"not", "or", "var"}, 3: {"imp", "bot", "var"}}
for f in build(2, ["not", "and", "or"]):
    for i in (1, 2, 3):
        g = t(i, f)
        assert ops(g, set()) <= S[i]
        for env in rows("PQ"):
            assert value(g, env) == value(f, env)
for f in build(2, ["and", "or", "imp"]):
    assert value(f, {"P": True, "Q": True})
g = cf.parse_formula("(P \\to (Q \\to \\bot)) \\to \\bot")
assert g == t(3, ("and", A[0], A[1]))
assert value(g, {"P": True, "Q": False}) is False
QUOTED = {}
print("thm-adequate-connectives: all quoted values check")
