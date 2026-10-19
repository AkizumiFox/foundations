"""exr-normal-forms-c3 (moved to Section 4.8, 08-completeness.md): (a), (d) valid, derivations of 10 and 9 lines without RAA;
(b), (c) refuted by the rows given."""
from _s0607_lib import S06, block, entails, parse, value, derivations
QUOTED = {"lines (a), (d)": [10, 9]}
assert entails(["(p \\to q) \\vee (p \\to r)"], "p \\to (q \\vee r)")
assert entails(["(p \\vee q) \\wedge \\neg p"], "q \\vee r")
env = {"P": True, "Q": False, "R": False}
assert value(parse("(p \\to q) \\to r"), env) and not value(parse("p \\to r"), env)
for q in (True, False):
    env = {"P": True, "Q": q, "R": False}
    assert value(parse("p \\vee (q \\wedge r)"), env) and not value(parse("(p \\vee q) \\wedge r"), env)
t = block(S06, "exr-normal-forms-c3")
assert [len(o) for o, _ in derivations(t)] == [10, 9]
assert "\\raa" not in t
print("exr-normal-forms-c3: all quoted values check")
