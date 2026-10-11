"""thm-classical-rules-interderivable (Ch 2 s05): the remark "without bot-E in the base list, LEM no
longer derives not-not-E" is stated without proof. Internal witness (for referees, not in the text):
read bot, and every negation, as always TRUE. Every primitive rule except bot-E and RAA then never
leads from true lines to a false one; every instance of LEM is true; and not-not-P |- P fails at P false."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}

def val(f, v):
    k = f[0]
    if k == "var":
        return v[f[1]]
    if k in ("bot", "not"):
        return True
    a, b = val(f[1], v), val(f[2], v)
    return {"and": a and b, "or": a or b, "imp": (not a) or b, "iff": a == b}[k]

for p in (False, True):
    v = {"P": p}
    assert val(Or(P, Not(P)), v)                      # LEM true
assert val(Not(Not(P)), {"P": False}) and not val(P, {"P": False})   # not-not-E fails
# not-E (phi, not phi |- bot) and not-I (anything |- not phi) are truth-preserving: bot, not are true.
# bot-E (bot |- phi) is not: bot true, phi false.
assert val(BOT, {"P": False}) and not val(P, {"P": False})
print("thm-classical-rules-interderivable: ok")
