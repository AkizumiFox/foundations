"""thm-monotonicity (Section 4.9): signs (def-occurrence-polarity) of the figure, the Quick
check and the drill; the theorem checked on random formulas over p, q, r by replacing each
signed occurrence of p and q by p or of p by p v q (both alpha |= beta); the examples
of the In-words paragraph; the warning's two rows."""
import random
from _logic import parse, val, rows, entails

def signs(f, s="+", path=()):
    """Yield (path, subformula, sign) for every node; sign is '+', '-' or None."""
    yield path, f, s
    k = f[0]
    flip = {"+": "-", "-": "+", None: None}
    if k == "not":
        yield from signs(f[1], flip[s], path + (1,))
    elif k in ("&", "|"):
        yield from signs(f[1], s, path + (1,))
        yield from signs(f[2], s, path + (2,))
    elif k == ">":
        yield from signs(f[1], flip[s], path + (1,))
        yield from signs(f[2], s, path + (2,))
    elif k == "=":
        yield from signs(f[1], None, path + (1,))
        yield from signs(f[2], None, path + (2,))

def atom_signs(text):
    return [(g[1], s) for _, g, s in signs(parse(text)) if g[0] == "atom"]

def replace(f, path, g):
    if not path:
        return g
    lst = list(f)
    lst[path[0]] = replace(f[path[0]], path[1:], g)
    return tuple(lst)

# the figure and the Quick check
assert atom_signs("(\\neg p \\to q) \\wedge \\neg r") == [("p", "+"), ("q", "+"), ("r", "-")]
assert atom_signs("\\neg(p \\to q) \\vee r") == [("p", "+"), ("q", "-"), ("r", "+")]
assert [s for _, g, s in signs(parse("(\\neg p \\to q) \\wedge \\neg r"))] == ["+", "+", "-", "+", "+", "+", "-"]
# drill (e), (f), (g)
assert atom_signs("\\neg(p \\to q)")[0] == ("p", "+")
assert atom_signs("(p \\to \\neg q) \\wedge r")[1] == ("q", "-")
assert atom_signs("p \\leftrightarrow q")[0] == ("p", None)

def ent(a, b):
    names = sorted({"p", "q", "r"})
    return all(val(b, v) for v in rows(names) if val(a, v))

PAIRS = [(parse("p \\wedge q"), parse("p")), (parse("p"), parse("p \\vee q"))]
random.seed(4)
def rand(d):
    if d == 0 or random.random() < 0.25:
        return random.choice([("atom", "p"), ("atom", "q"), ("atom", "r"), ("bot",),
                              ("&", ("atom", "p"), ("atom", "q"))])
    k = random.choice(["not", "&", "|", ">", "="])
    return ("not", rand(d - 1)) if k == "not" else (k, rand(d - 1), rand(d - 1))
checked = 0
for _ in range(3000):
    chi = rand(4)
    for alpha, beta in PAIRS:
        assert ent(alpha, beta)
        for path, g, s in list(signs(chi)):
            if g != alpha or s is None:
                continue
            chi2 = replace(chi, path, beta)
            if s == "+":
                assert ent(chi, chi2)
            else:
                assert ent(chi2, chi)
            checked += 1
assert checked > 500
# the In-words examples
assert not entails(["r \\to (p \\wedge q)"], "r \\to p")
assert not entails(["p \\to r"], "(p \\wedge q) \\to r")
# the warning: neither direction, with the two rows given
A, B = parse("(p \\wedge q) \\leftrightarrow r"), parse("p \\leftrightarrow r")
v1 = {"p": True, "q": False, "r": False}
v2 = {"p": True, "q": False, "r": True}
assert val(A, v1) and not val(B, v1)
assert val(B, v2) and not val(A, v2)
print("thm-monotonicity: all quoted values check")
